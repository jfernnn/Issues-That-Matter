from django import template
from opengraph import OpenGraph

register = template.Library()

@register.filter(name='video_url')
def video_url(value):
    embed_url = value.replace('watch?v=', 'embed/')
    return embed_url

@register.filter(name='color_change')
def color_change(value):
    print('remainder', value % 2)
    if value % 2 == 0:
        color = 'background-color:white'
    else:
        color = 'background-color:rgb(237,236,236)'
    return color
        