from django.shortcuts import render
from django.http import HttpResponse
from content.models import *

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    mymodel = Story.objects.get(id=1)
    return render(request, 'about.html', {'test': mymodel})

def programs(request):
    programs = Program.objects.all()
    print(programs)
    return render(request, 'programs/programs.html', { 'programs': programs })

def program_details(request, program: str):
    return render(request, 'programs/program-details.html', { "data": program})

def partners(request):
    return render(request, 'partners.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')
