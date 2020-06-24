from django import template
from opengraph import OpenGraph

register = template.Library()

@register.filter(name='video_url')
def video_url(value):
    embed_url = value.replace('watch?v=', 'embed/')
    return embed_url