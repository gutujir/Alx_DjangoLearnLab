from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book, Library


# Function-based view: return simple text
def list_books(request):
    books = Book.objects.all()
    response = "Books Available:\n"
    for book in books:
        response += f"{book.title} by {book.author.name}\n"
    return HttpResponse(response, content_type="text/plain")


# Class-based view: Library details with DetailView
class LibraryDetailView(DetailView):
    model = Library
    template_name = "library_detail.html"
    context_object_name = "library"
