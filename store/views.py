from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hellooo world! You're at the index page.")
