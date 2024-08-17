from django.test import SimpleTestCase
from django.urls import reverse, resolve
from orbit.views import (
  home, mission_and_vision, story_details, programs, program_details, partners,
  leadership, stories, contact, faq
)

class TestUrls(SimpleTestCase):

  def test_home_resolve(self):
    url = reverse('home')
    self.assertEqual(resolve(url).func, home)

  def test_mission_and_vision_resolve(self):
    url = reverse('mission_and_vision')
    self.assertEqual(resolve(url).func, mission_and_vision)

  def test_story_details_resolve(self):
    url = reverse('story_details', args=['test-slug'])
    self.assertEqual(resolve(url).func, story_details)

  def test_programs_resolve(self):
    url = reverse('programs')
    self.assertEqual(resolve(url).func, programs)

  def test_program_details_resolve(self):
    url = reverse('program_details', args=['test-slug'])
    self.assertEqual(resolve(url).func, program_details)

  def test_partners_resolve(self):
    url = reverse('partners')
    self.assertEqual(resolve(url).func, partners)

  def test_leadership_resolve(self):
    url = reverse('leadership')
    self.assertEqual(resolve(url).func, leadership)

  def test_stories_resolve(self):
    url = reverse('stories')
    self.assertEqual(resolve(url).func, stories)

  def test_contact_resolve(self):
    url = reverse('contact')
    self.assertEqual(resolve(url).func, contact)

  def test_faq_resolve(self):
    url = reverse('faq')
    self.assertEqual(resolve(url).func, faq)

  def test_story_details_with_special_characters_resolve(self):
    url = reverse('story_details', args=['special-@#!'])
    self.assertEqual(resolve(url).func, story_details)

  def test_program_details_with_special_characters_resolve(self):
    url = reverse('program_details', args=['special-@#!'])
    self.assertEqual(resolve(url).func, program_details)

  def test_invalid_url(self):
    with self.assertRaises(Exception):
      resolve('/invalid-url/')
