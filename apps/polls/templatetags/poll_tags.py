from django import template
from django.db.models import Count
from django.utils.safestring import mark_safe
from ..models import Poll
import markdown

register = template.Library()

@register.simple_tag
def total_polls():
    return Poll.objects.count()

@register.inclusion_tag('polls/poll_detail.html')
def show_latest_polls(count=5):
    latest_polls = Poll.objects.order_by('-publish')[:count]
    return {'latest_polls':latest_polls}