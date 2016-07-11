from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter(name='replace')
@stringfilter
def replace(value, arg):
    return value.replace(arg, '')


@register.filter(name='to_upper')
@stringfilter
def to_upper(value, arg):
    return "%s - %s" % (value.upper(), arg)
