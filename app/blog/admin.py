from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'created_at', 'updated_at')  # author alanını buraya ekledik

admin.site.register(Blog, BlogAdmin)