from django.test import TestCase, Client
from django.urls import reverse
from content.models import Post, FAQ
from executive.models import Program

class TestViews(TestCase):

  def setUp(self):
    self.client = Client()
    Program.objects.create(slug='program-slug')
    Post.objects.create(slug='story-slug')
    FAQ.objects.create(question='What is Django?', answer='A web framework.')

  def test_home(self):
    response = self.client.get(reverse('home'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html')

  def test_mission_and_vision(self):
    response = self.client.get(reverse('mission_and_vision'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'about/mission-and-vision.html')

  def test_partners(self):
    response = self.client.get(reverse('partners'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'about/partners.html')

  def test_leadership(self):
    response = self.client.get(reverse('leadership'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'about/leadership.html')

  def test_stories(self):
    response = self.client.get(reverse('stories'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'stories/stories.html')

  def test_story_details(self):
    url = reverse('story_details', args=['story-slug'])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'stories/story.html')
    response_404 = self.client.get(reverse('story_details', args=['test']))
    self.assertEqual(response_404.status_code, 404)

  def test_programs(self):
    response = self.client.get(reverse('programs'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'programs/programs.html')

  def test_program_details(self):
    url = reverse('program_details', args=['program-slug'])
    response = self.client.get(url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'programs/program-details.html')
    response_404 = self.client.get(reverse('program_details', args=['test']))
    self.assertEqual(response_404.status_code, 404)

  def test_contact(self):
    response = self.client.get(reverse('contact'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'contact.html')

  def test_faq(self):
    response = self.client.get(reverse('faq'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'faq.html')

  def test_sitemap(self):
    response = self.client.get(reverse('sitemap'))
    self.assertEqual(response.status_code, 200)
    self.assertEqual(response['Content-Type'], 'application/xml')
