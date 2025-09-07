# CRUD Operations for Book Model

This document demonstrates **Create, Retrieve, Update, and Delete (CRUD)** operations for the `Book` model in the `bookshelf` app using Django’s ORM.

---

## 1. Create

```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
book
# <Book: 1984 by George Orwell (1949)>

```

from bookshelf.models import Book

# Retrieve all Book instances

Book.objects.all()

# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

# Retrieve a single Book by title

book = Book.objects.get(title="1984")
book.title

# '1984'

book.author

# 'George Orwell'

book.publication_year

# 1949

from bookshelf.models import Book

# Fetch the existing book

book = Book.objects.get(title="1984")

# Update the title

book.title = "Nineteen Eighty-Four"
book.save()

book

# <Book: Nineteen Eighty-Four by George Orwell (1949)>

from bookshelf.models import Book

# Fetch the book by the updated title

book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book

book.delete()

# (1, {'bookshelf.Book': 1})

# Confirm deletion

Book.objects.all()

# <QuerySet []>
