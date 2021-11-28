from django.shortcuts import render
from .models import Book


def books_list_view(request):
    queryset = Book.objects.all()
    context = {"object_list": queryset}
    return render(request, "books/books_list.html", context)


def book_order_by(request):
    queryset = Book.objects.all().order_by('title_book', 'language', 'publishedData')
    context = {'object_order_by': queryset}
    return render(request, "books/books_list.html", context)
