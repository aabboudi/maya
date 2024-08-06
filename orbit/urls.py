from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('partners/', views.partners, name='partners'),
    path('leadership/', views.leadership, name='leadership'),
    path('stories/', views.stories, name='stories'),
    path('stories/<str:story>', views.story_details, name='story_details'),
    path('programs/', views.programs, name='programs'),
    path('programs/<str:program>/', views.program_details, name='program_details'),
    path('contact/', views.contact, name='contact'),
    path('frequently-asked-questions/', views.faq, name='faq'),
]
