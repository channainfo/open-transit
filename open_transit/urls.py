"""open_transit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.utils.translation import gettext as _

# prefix url with the language code
urlpatterns = i18n_patterns(

    path('', include('transit.urls', namespace='root') ),
    path('transit/', include('transit.urls', namespace='transit_root') ),
    path('admin/', admin.site.urls),
    prefix_default_language=True
)

# Serve upload file in dev (DEBUG=true)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
if(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


admin.site.index_title = _("Open Transit")
admin.site.site_header = _("Open Transit Admin")
admin.site.site_title  = _("Open Transit Management")