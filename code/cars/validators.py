from django.core.exceptions import ValidationError
import json
import requests
from django.apps import apps


def car_brand_validator(brand, model):
    url = f'https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformake/{brand}?format=json'
    response = requests.request("GET", url)
    response_data = json.loads(response.text)

    if response_data.get('Count') == 0:
        raise ValidationError(f'Invalid brand name: {brand}')

    found_models = list(filter(
        lambda request_model: request_model.get(
            'Model_Name').lower() == model.lower(),
        response_data.get('Results')
    ))

    if len(found_models) == 0:
        raise ValidationError(f'No models {model} found for brand: {brand}')

    [found_models] = found_models

    return found_models.get('Make_Name').capitalize(), found_models.get(
        'Model_Name')


def unique_registration_validator(registration):
    Car = apps.get_model('cars.Car')
    if Car.objects.filter(registration=registration).exists():
        raise ValidationError(f'Car with registration {registration} exists '
                              f'in database already')
