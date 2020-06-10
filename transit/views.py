from django.shortcuts import render

# Create your views here.
def index(request):
    context = {'data': "ok"}
    return render(request, 'transit/index.html', context)