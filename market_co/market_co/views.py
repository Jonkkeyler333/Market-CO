from django.http import HttpResponse,HttpResponseNotFound
from django.shortcuts import render

def error_404(request, exception):
   return HttpResponseNotFound("<h1>Page not found</h1><p>Sorry this page doesn't exist 😶‍🌫️</p>")