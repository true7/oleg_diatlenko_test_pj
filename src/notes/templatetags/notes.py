from django import template
from notes.models import Note

register = template.Library()

@register.inclusion_tag('base.html')
def get_note(pk):
    note = Note.objects.get(pk=pk)
    result = note.content
    return {'result': result}


'''
Have to be in dase.html, but do not work properly:

<div class='col-sm-6 col-sm-offset-3'>
{% for obj in object_list %}
<p>{% get_note obj.pk %}</p>
{% endfor %}
</div>
'''