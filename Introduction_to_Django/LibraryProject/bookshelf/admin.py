from django.contrib import admin
from .models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Fields to display in the admin list
    list_display = ("title", "author", "publication_year")

    # Add filtering options (right sidebar)
    list_filter = ("author", "publication_year")

    # Enable search by title and author
    search_fields = ("title", "author")
