from django.contrib import admin
from .models import Blog

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at')  # Göstermek istediğiniz alanları belirleyin
    search_fields = ('title', 'content')  # Arama yapabileceğiniz alanları belirleyin

admin.site.register(Blog, BlogAdmin)