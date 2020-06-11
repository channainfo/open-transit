from django.shortcuts import render
from django.utils.translation import gettext

# Create your views here.
def index(request):
    context = {'data': gettext("transit actor") }
    return render(request, 'transit/index.html', context)