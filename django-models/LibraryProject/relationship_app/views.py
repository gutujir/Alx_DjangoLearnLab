from .models import Library
from .models import Book, Author
from django.views.generic import DetailView
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required, user_passes_test


# Function-based view: Render book list
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


# Add book view
@permission_required('relationship_app.can_add_book')
def add_book(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        if title and author_id:
            author = get_object_or_404(Author, id=author_id)
            Book.objects.create(title=title, author=author)
            return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/add_book.html", {"authors": authors})


# Edit book view
@permission_required('relationship_app.can_change_book')
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        title = request.POST.get("title")
        author_id = request.POST.get("author")
        if title and author_id:
            book.title = title
            book.author = get_object_or_404(Author, id=author_id)
            book.save()
            return redirect("list_books")
    authors = Author.objects.all()
    return render(request, "relationship_app/edit_book.html", {"book": book, "authors": authors})


# Delete book view
@permission_required('relationship_app.can_delete_book')
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})

# Class-based view: Library details


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# User registration
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("list_books")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# User login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("list_books")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# User logout
@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")


# Role checks
def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
