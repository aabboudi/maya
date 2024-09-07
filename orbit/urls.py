from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticSitemap, ProgramSitemap, PostSitemap

sitemaps = {
    'static': StaticSitemap,
    'programs': ProgramSitemap,
    'stories': PostSitemap,
}

urlpatterns = [
    path('', views.home, name='home'),
    path('mission-and-vision/', views.mission_and_vision, name='mission_and_vision'),
    path('partners/', views.partners, name='partners'),
    path('leadership/', views.leadership, name='leadership'),
    path('stories/', views.stories, name='stories'),
    path('stories/<str:story>', views.story_details, name='story_details'),
    path('programs/', views.programs, name='programs'),
    path('programs/<str:program>/', views.program_details, name='program_details'),
    path('contact/', views.contact, name='contact'),
    path('message-sent/', views.message_sent, name='message_sent'),
    path('frequently-asked-questions/', views.faq, name='faq'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]
