from django.shortcuts import render
from books.models import Book
from datetime import datetime
from books.converters import PubDateConverter
from django.core.paginator import Paginator

date_converter = PubDateConverter()

def books_view(request):
    template = 'books/books_list.html'
    book_set = Book.objects.all()
    for book in book_set:
        book.pub_date =  date_converter.to_url(book.pub_date)
    context = {'books' : book_set}
    print(book_set)

    return render(request, template, context)

def view_book(request, date):
    template = 'books/book.html'
    date = date_converter.to_url(date)
    all_books = Book.objects.all()
    date_list = []
    for book in all_books:
        date_list.append(date_converter.to_url(book.pub_date))
    pagination = Paginator(date_list, 1)
    book = Book.objects.get(pub_date=date)
    book.pub_date = date_converter.to_url(book.pub_date)

    if date_list.index(book.pub_date) <= 0:
        current_page = 1
    else:
        current_page = date_list.index(book.pub_date) + 1
    
    page_object = pagination.page(current_page)

    if page_object.has_next():
        next_date = pagination.page(page_object.next_page_number()).object_list[0]
    else:
        next_date = ''

    if page_object.has_previous():
        prev_date = pagination.page(page_object.previous_page_number()).object_list[0]
    else:
        prev_date = ''


    context = {
        'book' : book,
        'next_date' : next_date,
        'prev_date' : prev_date
        }

    return render(request, template, context)
            