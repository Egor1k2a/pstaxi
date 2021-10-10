from django.utils.text import slugify
from unidecode import unidecode


def generate_unique_slug(model, value):
    unique_slug = slugify(unidecode(value if value else 'empty'), allow_unicode=True).lower()
    count = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{unique_slug}-{count}'
        count += 1

    return unique_slug
