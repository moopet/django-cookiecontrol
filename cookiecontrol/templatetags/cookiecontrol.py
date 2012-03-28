from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('cookiecontrol.html')
def cookiecontrol():
    countries = settings.COOKIECONTROL_COUNTRIES

    return {
        'shape': settings.COOKIECONTROL_SHAPE if hasattr(settings, 'COOKIECONTROL_SHAPE') else 'triangle',
        'position': settings.COOKIECONTROL_POSITION if hasattr(settings, 'COOKIECONTROL_POSITION') else 'left',
        'hide_on_accept': settings.COOKIECONTROL_HIDE if hasattr(settings, 'COOKIECONTROL_HIDE') else False,
        'hide_after': settings.COOKIECONTROL_HIDE_AFTER if hasattr(settings, 'COOKIECONTROL_HIDE_AFTER') else 30,
        'start_open': settings.COOKIECONTROL_START_OPEN if hasattr(settings, 'COOKIECONTROL_START_OPEN') else False,
        'privacy_url': settings.COOKIECONTROL_PRIVACY_URL,
        'countries': countries if not isinstance(countries, str) else [countries,],
    }
