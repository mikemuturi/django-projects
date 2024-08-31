from django.views.generic import ListView
from django.shortcuts import render

from books.models import Book

# Create your views here.
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    