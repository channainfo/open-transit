from django.db import models
from django.contrib.postgres.indexes import GinIndex
from modeltrans.fields import TranslationField

from django.conf import settings
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    short_description = models.CharField(max_length=255)
    description = models.TextField(max_length=60000)
    about = models.CharField(max_length=255)

    slug = models.CharField(max_length=255)
    i18n = TranslationField(fields=("name", "short_description", "description", "about"))


    def __str__(self):
        return self.name

    class Meta:
        indexes = [GinIndex(fields=["i18n"]), ]
