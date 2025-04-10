from django.shortcuts import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hello world, you are at poll index')
