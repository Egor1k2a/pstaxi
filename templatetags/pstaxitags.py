from django import template
from django.template import defaultfilters

from utils.text import plural_form

register = template.Library()


@register.filter
def pstaxidate(date):
    return defaultfilters.date(date, "d.m.Y г.")


@register.simple_tag
def plural(value, form1, form2, form5):
    return plural_form(value, form1, form2, form5)
