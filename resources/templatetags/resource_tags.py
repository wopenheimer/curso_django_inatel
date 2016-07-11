from django import template

register = template.Library()

@register.simple_tag
def get_vehicles(number_items):
    list_vehicle = list()
    list_vehicle.append('Palio')
    list_vehicle.append('Fusca')
    list_vehicle.append('Brasilia')

    return list_vehicle[:number_items]
