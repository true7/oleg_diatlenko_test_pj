from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.list import ListView

from .models import Note
from .forms import NoteForm


class NoteListView(ListView):
    form_class = NoteForm
    template_name = 'base.html'
    model = Note
    context_object_name = 'object_list'

    def get_context_data(self, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        context['form'] = self.form_class
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('notes:list'))
        return render(
                request,
                self.template_name,
                {self.context_object_name: self.get_queryset(), 'form': form}
                )
