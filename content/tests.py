from datetime import date
from django.test import TestCase
from django.urls import reverse
from .models import Person, Post, PostImage, Project, Program, ProgramGoal, FAQ, Banner

class PersonModelTest(TestCase):
  def setUp(self):
    self.person = Person.objects.create(
      name="John Doe",
      title="Editor"
    )

  def test_person_creation(self):
    self.assertIsInstance(self.person, Person)
    self.assertEqual(str(self.person), "John Doe")

  def test_default_avatar(self):
    self.assertEqual(self.person.avatar, 'people/default-avatar.png')

  def test_auto_dates(self):
    self.assertIsNotNone(self.person.created_at)
    self.assertIsNotNone(self.person.updated_at)

class PostModelTest(TestCase):
  def setUp(self):
    self.person = Person.objects.create(name="Jane Doe", title="Author")
    self.post = Post.objects.create(
      title="Sample Post",
      slug="sample-post",
      description="A sample blog post.",
      content="Detailed content of the blog post."
    )
    self.post.author.add(self.person)

  def test_post_creation(self):
    self.assertIsInstance(self.post, Post)
    self.assertEqual(str(self.post), "Sample Post")

  def test_slug_field(self):
    self.assertEqual(self.post.slug, "sample-post")

  def test_category_default_value(self):
    self.assertEqual(self.post.category, "Blog")

  def test_post_author_relationship(self):
    self.assertIn(self.person, self.post.author.all())

  def test_get_absolute_url(self):
    url = self.post.get_absolute_url()
    self.assertEqual(url, reverse('story_details', args=['sample-post']))

  def test_auto_dates(self):
    self.assertIsNotNone(self.post.created_at)
    self.assertIsNotNone(self.post.updated_at)

class PostImageModelTest(TestCase):
  def setUp(self):
    self.post = Post.objects.create(title="Image Post", slug="image-post")
    self.post_image = PostImage.objects.create(post=self.post, image="stories/sample.jpg")

  def test_post_image_creation(self):
    self.assertIsInstance(self.post_image, PostImage)
    self.assertEqual(self.post_image.post, self.post)
    self.assertEqual(self.post_image.image, "stories/sample.jpg")

class ProjectModelTest(TestCase):
  def setUp(self):
    self.project = Project.objects.create(
      title="Sample Project",
      slug="sample-project",
      description="This is a sample project.",
      location="Sample Location",
      start_date=date.today(),
      end_date=date.today()
    )

  def test_project_creation(self):
    self.assertIsInstance(self.project, Project)
    self.assertEqual(str(self.project), "Sample Project")

  def test_slug_field(self):
    self.assertEqual(self.project.slug, "sample-project")

  # def test_get_absolute_url(self):
  #   url = reverse('program_details', args=['sample-project'])
  #   self.assertEqual(url, self.project.get_absolute_url())

  def test_auto_dates(self):
    self.assertIsNotNone(self.project.created_at)
    self.assertIsNotNone(self.project.updated_at)

class ProgramModelTest(TestCase):
  def setUp(self):
    self.project = Project.objects.create(
      title="Related Project",
      slug="related-project",
      start_date="2023-01-01",
      end_date="2023-12-31"
    )
    self.program = Program.objects.create(
      active=True,
      title="Sample Program",
      slug="sample-program",
      description="This is a sample program.",
      manager="John Doe"
    )
    self.program.projects.add(self.project)

  def test_program_creation(self):
    self.assertIsInstance(self.program, Program)
    self.assertEqual(str(self.program), "Sample Program")

  def test_slug_field(self):
    self.assertEqual(self.program.slug, "sample-program")

  def test_get_absolute_url(self):
    url = self.program.get_absolute_url()
    self.assertEqual(url, reverse('program_details', args=['sample-program']))

  def test_program_project_relationship(self):
    self.assertIn(self.project, self.program.projects.all())

  def test_auto_dates(self):
    self.assertIsNotNone(self.program.created_at)
    self.assertIsNotNone(self.program.updated_at)

class ProgramGoalModelTest(TestCase):
  def setUp(self):
    self.program = Program.objects.create(
      active=True,
      title="Program with Goals",
      slug="program-with-goals",
      description="This is a sample program with goals.",
      manager="John Doe"
    )
    self.program_goal = ProgramGoal.objects.create(
      goal="Increase Engagement",
      icon="icon-engagement",
      description="Goal to increase engagement by 20%.",
      image="programs/engagement.jpg",
      program=self.program
    )

  def test_program_goal_creation(self):
    self.assertIsInstance(self.program_goal, ProgramGoal)
    self.assertEqual(str(self.program_goal), "Increase Engagement")

  def test_program_goal_fields(self):
    self.assertEqual(self.program_goal.icon, "icon-engagement")
    self.assertEqual(self.program_goal.description, "Goal to increase engagement by 20%.")

  def test_program_goal_relationship(self):
    self.assertEqual(self.program_goal.program, self.program)

  def test_auto_dates(self):
    self.assertIsNotNone(self.program_goal.created_at)
    self.assertIsNotNone(self.program_goal.updated_at)

class FAQModelTest(TestCase):
  def setUp(self):
    self.faq = FAQ.objects.create(
      question="What is the purpose of this FAQ?",
      answer="To answer common questions."
    )

  def test_faq_creation(self):
    self.assertIsInstance(self.faq, FAQ)
    self.assertEqual(str(self.faq), "What is the purpose of this FAQ?")

  def test_faq_fields(self):
    self.assertEqual(self.faq.question, "What is the purpose of this FAQ?")
    self.assertEqual(self.faq.answer, "To answer common questions.")

  def test_auto_dates(self):
    self.assertIsNotNone(self.faq.created_at)
    self.assertIsNotNone(self.faq.updated_at)

class BannerModelTest(TestCase):
  def setUp(self):
    self.banner = Banner.objects.create(
      active=True,
      text="Welcome to our website",
      cta="Learn More",
      cta_type="url",
      cta_link="https://example.com",
      color="blue"
    )

  def test_banner_creation(self):
    self.assertIsInstance(self.banner, Banner)
    self.assertEqual(str(self.banner.text), "Welcome to our website")

  def test_default_active_status(self):
    banner = Banner.objects.create(
      text="Inactive Banner",
      cta="Click Here",
      cta_type="slug",
      cta_link="/contact"
    )
    self.assertFalse(banner.active)

  def test_cta_type_choices(self):
    banner_slug = Banner.objects.create(
      text="Relative CTA",
      cta="Visit",
      cta_type="slug",
      cta_link="/home"
    )
    banner_url = Banner.objects.create(
      text="Absolute CTA",
      cta="Visit",
      cta_type="url",
      cta_link="https://example.com"
    )
    self.assertEqual(banner_slug.cta_type, "slug")
    self.assertEqual(banner_url.cta_type, "url")

  def test_color_field(self):
    banner_with_color = Banner.objects.create(
      text="Colored Banner",
      cta="Check",
      cta_type="url",
      cta_link="https://example.com",
      color="red"
    )
    banner_no_color = Banner.objects.create(
      text="No Color Banner",
      cta="Check",
      cta_type="url",
      cta_link="https://example.com",
      color=None
    )
    self.assertEqual(banner_with_color.color, "red")
    self.assertIsNone(banner_no_color.color)

  def test_auto_created_at(self):
    self.assertIsNotNone(self.banner.created_at)
