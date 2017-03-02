from .models import Note

def total_count(request):
    total = Note.objects.count()
    return {
        'total': total,
        'total_label': 'Total count of all notes: ',
    }