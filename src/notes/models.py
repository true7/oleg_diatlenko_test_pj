from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

class Note(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=200, validators=[MinLengthValidator(10)])
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-timestamp']
