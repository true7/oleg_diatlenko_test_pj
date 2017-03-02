from django.shortcuts import render
from django.views import View

from .models import Note


class ListView(View):

    def get(self, request, *args, **kwargs):
        instance = Note.objects.all()
        context = {
            'object_list': instance,
        }
        return render(request, 'base.html', context=context)

    def post(self, request, *args, **kwargs):
        pass
