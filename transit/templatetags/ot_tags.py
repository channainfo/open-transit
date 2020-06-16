from django.conf import settings
from django import template

from ..app_helper import switch_lang_url

register = template.Library()

@register.simple_tag
def ot_settings(name):
    return getattr(settings, name, "")

@register.simple_tag
def ot_languages():
    return getattr(settings, "LANGUAGES", [])

@register.filter
def switch_i18n_prefix(path, language):
    """takes in a string path"""
    return switch_lang_url(path, language)
 
@register.filter
def switch_i18n(request, language):
    """takes in a request object and gets the path from it"""
    return switch_i18n_prefix(request.get_full_path(), language)
