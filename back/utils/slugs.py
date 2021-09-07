from django.utils.crypto import get_random_string
from django.utils.text import slugify


def generate_slug():
    return get_random_string(10)
    

def append_slug(title):
    return slugify(title) + '-' + get_random_string(7)
