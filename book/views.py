from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm
from order.models import Order
from rest_framework import viewsets
from .serializers import BookSerializer


def books(request):
    return render(request, 'book/books.html', {'books': Book.objects.all()})


def book_item(request, book_id):
    book = Book.objects.get(pk=book_id)
    amount_left = book.count - Order.objects.filter(book=book_id, end_at=None).count()

    context = {'title': book.name, 'id': book.id, 'authors': book.authors.all(),
               'count': book.count, 'amount_left': amount_left}

    return render(request, 'book/book_details.html', context)


def create_book(request):
    if request.method != 'POST':
        new_book = BookForm()
        error = ''
    else:
        new_book = BookForm(request.POST)
        if new_book.is_valid() and new_book.book_check():
            book_id = new_book.save().id
            return redirect('/books/', book_id)
        else:
            error = 'Form is incorrect!'

    context = {'book': new_book, 'error': error}
    return render(request, 'book/create_book.html', context)


def update_book(request, pk):
    if request.method != 'POST':
        updated_book = BookForm(instance=Book.get_by_id(pk))
        error = ''
    else:
        updated_book = BookForm(request.POST, instance=Book.get_by_id(pk))
        if updated_book.is_valid() and updated_book.book_check():
            book_id = updated_book.save().id
            return redirect('/books/', book_id)
        else:
            error = 'Form is incorrect'

    context = {'book': updated_book, 'error': error}
    return render(request, 'book/create_book.html', context)


def delete_book(request, pk):
    Book.delete_by_id(pk)
    return redirect('/books/')


class BookView(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
