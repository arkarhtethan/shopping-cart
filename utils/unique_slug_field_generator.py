from .random_string_generator import random_string_generator
from django.utils.text import slugify

def unique_slug_generator(instance, new_slug=None):

    if new_slug is not None:

        slug = new_slug

    else:

        slug = slugify(instance)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug=slug).exists()

    if qs_exists:
        new_slug = "{slug}-{randstr}".format(
            slug=slug,
            randstr=random_string_generator(size=4)
        )
        return unique_slug_generator(instance, new_slug=new_slug)

    return slug
