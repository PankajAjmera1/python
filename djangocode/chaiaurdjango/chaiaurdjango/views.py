from django.http import HttpResponse
from django.shortcuts import render


def home(request):
   # return HttpResponse("Hello, Django!")   
    return render(request, 'index.html')

def about(request):
    return HttpResponse("About Django!")