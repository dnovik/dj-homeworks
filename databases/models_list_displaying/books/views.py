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
    current_date = request.path.split('/')[2]
    current_page = page.page()
    print(date_list.index(current_date))
    
    context = {
        'book' : book,
        'next_page' : page,
        'prev_page' : page}

    return render(request, template, context)
            
methods = ['COOKIES', 'FILES', 'GET', 'META', 'POST', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_encoding', '_get_post', '_get_raw_host', '_get_scheme', '_initialize_handlers', '_load_post_and_files', '_mark_post_parse_error', '_messages', '_post_parse_error', '_read_started', '_set_post', '_stream', '_upload_handlers', 'body', 'build_absolute_uri', 'close', 'content_params', 'content_type', 'csrf_processing_done', 'encoding', 'environ', 'get_full_path', 'get_host', 'get_port', 'get_raw_uri', 'get_signed_cookie', 'is_ajax', 'is_secure', 'method', 'parse_file_upload', 'path', 'path_info', 'read', 'readline', 'readlines', 'resolver_match', 'scheme', 'session', 'upload_handlers', 'user', 'xreadlines']