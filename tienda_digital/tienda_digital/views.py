from django.shortcuts import render
from django.http import HttpResponse

#Rest Framework
from rest_framework.decorators import api_view
from rest_framework.response import Response

def index(request):
    return render(request, 'index.html')