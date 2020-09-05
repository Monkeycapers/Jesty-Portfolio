from django import template
import mistune

register = template.Library()

@register.filter
def markdown(value):
    renderer = mistune.Renderer(escape=True)
    markdown = mistune.Markdown(renderer = renderer)
    return markdown(value)