from bookshelf.models import Book

Book.objects.all()

# <QuerySet [<Book: 1984 by George Orwell (1949)>]>

book = Book.objects.get(title="1984")
book.title

# '1984'

book.author

# 'George Orwell'

book.publication_year

# 1949
