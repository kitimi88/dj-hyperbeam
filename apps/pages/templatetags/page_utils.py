from django import template
import readtime
from datetime import datetime


register = template.Library()

def read(html):
    return readtime.of_html(html)

register.filter('readtime',read)

@register.filter
def time_based_greeting(value):
    current_hour = datetime.now().hour

    if current_hour < 12:
        return "Good morning"
    elif current_hour < 18:
        return "Good afternoon"
    else:
        return "Good evening"
