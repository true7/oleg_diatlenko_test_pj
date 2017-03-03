from django.contrib import admin

from .models import Note, Book

class NoteModel(admin.ModelAdmin):
    list_display = ["title", "user", "timestamp", 'image']
    list_display_links = ["user"]
    list_editable = ["title"]
    list_filter = ["timestamp"]
    search_fields = ["title", "content"]

    class Meta:
        model = Note


admin.site.register(Note, NoteModel)
admin.site.register(Book)
