from django.shortcuts import render
from .models import Book
from .filters import BookFilter

def books(request):
    books = Book.objects.all()
    book_filter = BookFilter(request.GET, queryset=books)
    return render(request, 'books.html', {
        'book_filter': book_filter
        })