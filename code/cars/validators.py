from django.core.exceptions import ValidationError
import json
import requests


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
