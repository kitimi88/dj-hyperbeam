from django import template
from django.utils import timezone
import readtime
import math

register = template.Library()


def read(html):
    return readtime.of_html(html)

register.filter('readtime',read)

