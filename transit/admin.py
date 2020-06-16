from django.contrib import admin
from modeltrans.admin import ActiveLanguageMixin
from .models import Company

from django.utils.translation import gettext_lazy as _

@admin.register(Company)
class CompanyAdmin(ActiveLanguageMixin, admin.ModelAdmin):
    # fields        = ('name', 'short_description', 'description', 'about')
    list_display  = ('name', 'short_description', 'description', 'about')

    list_filter   = ( 'name', 'short_description', 'about' )
    search_fields = ( 'name', 'short_description', 'about')

# Register your models here.
# admin.site.register(Company, CompanyAdmin)
