from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author_name', 'created_at')  # author alanını buraya ekledik

admin.site.register(Blog, BlogAdmin)