from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.db.models import Count

from colleges.models import SignificantMajors, College, Blog


def index(request):
    return render(request, 'index.html', {})

def schools_list(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'colleges.html', context)

def resources(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'resources.html', context)

def faq(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'faq.html', context)

def checklist(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'checklist.html', context)

def ambassadors(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'ambassadors.html', context)

def schools(request):
    colleges = College.objects.order_by('name')
    context = {'colleges': colleges}
    return render(request, 'schools.html', context)

def college_comparison(request):
    return render (request, 'colleges/college_comparison.html', {})
    search_bar = SearchBar(request, ['college'])

def college_blog(request):
    return render (request, 'colleges/college_blog.html', {})

def home(request):
    return render(request, 'home.html', {})
