from django import template
from django.utils.http import urlencode

from books.models import Category

register = template.Library()

@register.filter
def fillzero(value):
    return f'{value:05}'

@register.simple_tag()
def all_categories():
    return Category.objects.all()

@register.simple_tag(takes_context=True)
def extend_param(context, **kwargs):
    query = context.get('request').GET.dict()
    query.update(kwargs)
    return urlencode(query)