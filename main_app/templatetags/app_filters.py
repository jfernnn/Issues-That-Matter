from django import template
from opengraph import OpenGraph

register = template.Library()

@register.filter(name='og_title')
def og_title(value):
    og = OpenGraph(value)
    return og.title

@register.filter(name='og_description')
def og_description(value):
    og = OpenGraph(value)
    return og.description

@register.filter(name='og_image')
def og_image(value):
    og = OpenGraph(value)
    return og.image
    