from django import template
from notes.models import Note

register = template.Library()

@register.inclusion_tag('base.html')
def get_note(pk):
    note = Note.objects.get(pk=pk)
    result = note.content
    return {'result': result}

