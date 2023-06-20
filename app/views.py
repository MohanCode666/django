from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def an(request):
    return HttpResponse('hiii')
def mark(request):
    return render(request,'men.html')