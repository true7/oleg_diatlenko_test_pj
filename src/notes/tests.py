from django.test import TestCase
from django.core.urlresolvers import reverse

from .models import Note
from .forms import NoteForm


class NoteTestCase(TestCase):
    def setUp(self):
        Note.objects.create(title='Test title', content='Test content', image='cat.png')

    def test_note_title_content(self):
        '''
        Test note creation, test of UpperCharField, test ImageField.
        '''
        obj = Note.objects.get(title='Test title')
        self.assertEqual(obj.title, 'Test title'.upper())
        self.assertTrue(obj.content == 'Test content')
        self.assertEqual(obj.image.name, 'cat.png')
        self.assertFalse(obj.image.name == 'dog.png')
        self.assertTrue(obj.image.url == '/media/cat.png') # will remove later

    def test_string_representation(self):
        note = Note.objects.get(title='Test title')
        self.assertEqual(str(note), note.title)

    def test_list_view(self):
        '''
        Test status code for list_view.
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_notes_count(self):
        '''
        Checks count of the notes.
        '''
        response = self.client.get('/')
        self.assertTrue('object_list' in response.context)
        object_list = Note.objects.count()
        object_list_from_context = len(response.context['object_list'])
        self.assertEqual(object_list, object_list_from_context)


class NoteFormTestCase(TestCase):
    def test_valid_form(self):
        '''
        Testing form validation.
        '''
        title = 'A new title'
        content  = 'Some test content'
        obj = Note.objects.create(title=title, content=content)
        data = {'title': obj.title, "content": obj.content}
        form = NoteForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data.get('title'), obj.title)
        self.assertNotEqual(form.cleaned_data.get("content"), "Another item")

    def test_invalid_form(self):
        '''
        Testing form invalidation.
        '''
        title = 'Another new title'
        content  = 'Content' # Less than 10 symbols
        obj = Note.objects.create(title=title, content=content)
        data = {'title': obj.title, "content": obj.content}
        form = NoteForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.errors)

    def test_adding_new_note(self):
        '''
        Test note will be added succesfully to database.
        '''
        count = Note.objects.count()
        title = 'A very new title'
        content  = 'Some new test content'
        obj = Note.objects.create(title=title, content=content)
        data = {'title': obj.title, "content": obj.content}
        form = NoteForm(data=data)
        new_count = Note.objects.count()
        self.assertEqual(count+1, new_count)


