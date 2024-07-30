from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('programs/', views.programs, name='programs'),
    path('programs/<str:program>/', views.program_details, name='program_details'),
    path('contact/', views.contact, name='contact'),
    path('partners/', views.partners, name='partners'),
    path('faq/', views.faq, name='faq'),
]
