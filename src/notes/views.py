from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect

from .models import Note
from .forms import NoteForm


class ListView(View):

    def get(self, request, *args, **kwargs):
        form = NoteForm()
        instance = Note.objects.all()
        context = {
            'object_list': instance,
            'form': form,
        }
        return render(request, 'base.html', context=context)

    def post(self, request, *args, **kwargs):
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
