from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from orbit.views import (
  home, mission_and_vision, story_details, programs, program_details, partners,
  leadership, stories, contact, message_sent, faq
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

  def test_message_sent_resolve_without_flag(self):
    url = reverse('message_sent')
    self.assertEqual(resolve(url).func, message_sent)

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

class ContactFormTests(TestCase):
  def test_contact_form_submission_and_redirect(self):
    # Add test cases where form is invalid
    response = self.client.post(reverse('contact'), data={
      'first_name': 'John',
      'last_name': 'Doe',
      'email': 'johndoe@email.com',
      'phone_number': '123456789',
      'message': 'This is a test message.',
      'privacy_policy': 'on'
    })
    
    self.assertEqual(response.status_code, 200)
    # self.assertRedirects(response, reverse('message_sent'))
    self.assertTemplateUsed(response, 'contact/message-sent.html')

  def test_message_sent_redirect_with_flag(self):
    session = self.client.session
    session['message_sent_flag'] = True
    session.save()
    response = self.client.get(reverse('message_sent'))
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'contact/message-sent.html')

  def test_message_sent_redirect_without_flag(self):
    response = self.client.get(reverse('message_sent'))
    self.assertEqual(response.status_code, 302)
    self.assertRedirects(response, '/')
