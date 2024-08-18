from django.test import TestCase
from .models import BoardMember, Manager
from content.models import Program

class BoardMemberModelTest(TestCase):
  def setUp(self):
    self.board_member = BoardMember.objects.create(
      active=True,
      name="John Doe",
      title="Chairman",
      bio="Experienced leader in the industry."
    )

  def test_board_member_creation(self):
    self.assertIsInstance(self.board_member, BoardMember)
    self.assertEqual(str(self.board_member), "John Doe")

  def test_board_member_default_avatar(self):
    self.assertEqual(self.board_member.avatar, 'people/default-avatar.png')

  def test_board_member_fields(self):
    self.assertTrue(self.board_member.active)
    self.assertEqual(self.board_member.name, "John Doe")
    self.assertEqual(self.board_member.title, "Chairman")
    self.assertEqual(self.board_member.bio, "Experienced leader in the industry.")

  def test_auto_dates(self):
    self.assertIsNotNone(self.board_member.created_at)
    self.assertIsNotNone(self.board_member.updated_at)

class ManagerModelTest(TestCase):
  def setUp(self):
    self.program = Program.objects.create(
      title="Sample Program", 
      description="This is a sample program."
    )
    self.manager = Manager.objects.create(
      active=True,
      name="Jane Doe",
      program=self.program,
      bio="Program manager with extensive experience."
    )

  def test_manager_creation(self):
    self.assertIsInstance(self.manager, Manager)
    self.assertEqual(str(self.manager), "Jane Doe")

  def test_manager_default_avatar(self):
    self.assertEqual(self.manager.avatar, 'people/default-avatar.png')

  def test_manager_fields(self):
    self.assertTrue(self.manager.active)
    self.assertEqual(self.manager.name, "Jane Doe")
    self.assertEqual(self.manager.program, self.program)
    self.assertEqual(self.manager.bio, "Program manager with extensive experience.")

  def test_auto_dates(self):
    self.assertIsNotNone(self.manager.created_at)
    self.assertIsNotNone(self.manager.updated_at)

  def test_manager_program_relationship(self):
    self.assertEqual(self.manager.program.title, "Sample Program")
