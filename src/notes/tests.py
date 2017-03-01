from django.test import TestCase
from .models import Note


class NoteTestCase(TestCase):
    def setUp(self):
        Note.objects.create(title='Test title', content='Test content')

    def test_note_title_content(self):
        """Test note creation."""
        obj = Note.objects.get(title='Test title')
        self.assertEqual(obj.title, 'Test title')
        self.assertTrue(obj.content == 'Test content')

    def test_list_view(self):
        """Test status code for list_view."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_count(self):
        """Checks count of the notes."""
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        object_list = Note.objects.count()
        object_list_from_context = len(response.context['object_list'])
        self.assertEqual(object_list, object_list_from_context)

