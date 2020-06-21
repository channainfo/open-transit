from django.contrib import admin
from django.utils.html import format_html
from modeltrans.admin import ActiveLanguageMixin
from .models import Company
from .models import UserProfile

from django.utils.translation import gettext_lazy as _

@admin.register(Company)
class CompanyAdmin(ActiveLanguageMixin, admin.ModelAdmin):
    # fields        = ('name', 'short_description', 'description', 'about')
    list_display  = ('name', 'short_description', 'description', 'about')

    list_filter   = ( 'name', 'short_description', 'about' )
    search_fields = ( 'name', 'short_description', 'about')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'profile_pic_url', 'avatar', )

    def profile_pic_url(self, obj):
        return obj.profile_pic.url

    def avatar(self, obj):
        return format_html("<img src='{}' alt='{}' width=32 style='border: 1px solid #ccc;'/>", obj.profile_pic.url, obj.profile_pic.name )


# Register your models here.
# admin.site.register(Company, CompanyAdmin)
