from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Eğer blog yazarı kullanıcı modeli ise

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title