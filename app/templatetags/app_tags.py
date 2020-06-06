from django import template

register = template.Library()


@register.filter
def active_page_class(page, path):
    if page == path:
        return 'active'
    else:
        return ''
