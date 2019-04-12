from django import template

register = template.Library()

@register.filter
def filter_by_member(consumption, name):
    return consumption.filter(team_member=name).distinct()
