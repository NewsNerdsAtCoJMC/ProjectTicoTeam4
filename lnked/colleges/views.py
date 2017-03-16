from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.db.models import Count

from colleges.models import SignificantMajors, College, Blog


def index(request):
    return HttpResponse("Hello, world. You're at the homepage.")
