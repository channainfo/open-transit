from django.db import models
from django.contrib.postgres.indexes import GinIndex
from modeltrans.fields import TranslationField

from django.utils.translation import gettext as _

from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.

class Company(models.Model):
    name = models.CharField(
                            max_length=255, 
                            help_text=_('First name and last name'),
                            verbose_name=_('name'))

    short_description = models.CharField(
                            max_length=255,
                            help_text=_('Short description to display in the summary'),
                            verbose_name=_('Short description')
                            )
    description = models.TextField(max_length=60000)
    about = models.CharField(max_length=255)

    phone = models.CharField(
                            max_length=11,
                            null=True,
                            blank=True,
                            validators=[RegexValidator( '^\d{10,11}$', _('Phone must be exactly 10 digits.'))],
                            verbose_name=_('phone number'))

    slug = models.CharField(max_length=255)
    i18n = TranslationField(fields=("name", "short_description", "description", "about"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _ ('Companies')
        indexes = [GinIndex(fields=["i18n"]), ]
