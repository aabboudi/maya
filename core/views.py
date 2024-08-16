# from django.shortcuts import render

# def error_404(request, exception):
#     return render(request, 'error_404.html')

from django.http import HttpResponse
def error_404(request, exception):
    return HttpResponse('<h1>Custom 404 error</h1>', status=404)
