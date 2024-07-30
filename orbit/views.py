from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')
    # return HttpResponse("Hello, world. You're at the polls index.")

def about(request):
    return render(request, 'about.html')

def programs(request):
    return render(request, 'programs/programs.html')

def program_details(request, program: str):
    return render(request, 'programs/program-details.html', { "data": program})

def partners(request):
    return render(request, 'partners.html')

def contact(request):
    return render(request, 'contact.html')

def faq(request):
    return render(request, 'faq.html')
