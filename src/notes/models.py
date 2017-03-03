from django.db import models
from django.conf import settings
from django.db.models.signals import post_delete
from django.core.validators import MinLengthValidator


class UpperCharField(models.CharField):
    def get_prep_value(self, value):
        value = super(UpperCharField, self).get_prep_value(value)
        return value.upper()


class Note(models.Model):
    title = UpperCharField(max_length=20)
    content = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    image = models.ImageField(null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']


class Book(models.Model):
    headline = models.CharField(max_length=20)
    notes = models.ManyToManyField(Note)
         
    def __str__(self):
        return self.headline

    class Meta:
        ordering = ('headline',)


def book_cascade_delete(sender, **kwargs):
    qs = Book.objects.filter(notes__isnull=True)
    qs.delete()

post_delete.connect(book_cascade_delete, sender=Note)