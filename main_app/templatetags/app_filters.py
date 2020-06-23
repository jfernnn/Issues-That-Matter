from django import template
from opengraph import OpenGraph

register = template.Library()

@register.filter(name='og_title')
def og_title(value):
    og = OpenGraph(value)
    print(og)
    return og.title

@register.filter(name='og_description')
def og_description(value):
    og = OpenGraph(value)
    return og.description

@register.filter(name='og_image')
def og_image(value):
    og = OpenGraph(value)
    return og.image
    
@register.filter(name='og_type')
def og_type(value):
    og = OpenGraph(value)
    return og.type
    
@register.filter(name='video_url')
def video_url(value):
    embed_url = value.replace('watch?v=', 'embed/')
    return embed_url