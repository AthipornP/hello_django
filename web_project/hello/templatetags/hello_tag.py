from django import template

register = template.Library()


@register.inclusion_tag("tags/hello.html")
def hello():
    ...