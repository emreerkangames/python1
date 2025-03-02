from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User  # Eğer blog yazarı kullanıcı modeli ise

class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Eğer blog yazarı bir kullanıcı ise
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def author_name(self):
        return self.author.username  # Yazarın ismini göstermek için