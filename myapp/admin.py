from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'author', 'year')

admin.site.register(Book, BookAdmin)