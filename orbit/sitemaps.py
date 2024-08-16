import datetime
from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from content.models import Program, Post

class BaseSitemap(Sitemap):
  priority = 0.9
  changefreq = 'monthly'

  def lastmod(self, obj):
    return obj.updated_at

class ProgramSitemap(BaseSitemap):
  def items(self):
    return Program.objects.all().order_by('updated_at')

class PostSitemap(BaseSitemap):
  def items(self):
    return Post.objects.all().order_by('updated_at')

class StaticSitemap(Sitemap):
  priority = 1.0
  changefreq = 'monthly'

  def items(self):
    return [
      'home',
      'mission_and_vision',
      'partners',
      'stories',
      'programs',
      'contact',
      'faq',
    ]

  def location(self, item):
    return reverse(item)
  
  def lastmod(self, items):
    return datetime.datetime.now()
