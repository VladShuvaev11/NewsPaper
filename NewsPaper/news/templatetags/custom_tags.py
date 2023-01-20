from django import template
from datetime import datetime


register = template.Library()


@register.simple_tag()
def current_date(date_format='%b %d %Y'):
    return datetime.utcnow().strftime(date_format)


