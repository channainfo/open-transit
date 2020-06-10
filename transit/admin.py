from django.contrib import admin
from modeltrans.admin import ActiveLanguageMixin
from .models import Company

class CompanyAdmin(ActiveLanguageMixin, admin.ModelAdmin):
    pass
# Register your models here.

admin.site.register(Company, CompanyAdmin)
