from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.core.paginator import Paginator


from books.models import Category, Book


def index(request) -> HttpResponse:

    return render(
        request,
        'books/index.html',
        {'title': 'HomePage', 'content': 'BookStore'}
    )

def books(request, category_slug) -> HttpResponse:
    books = Book.objects.filter(category__slug=category_slug)

    page_number = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale')
    order_by = request.GET.get('order_by')

    if order_by and order_by != 'default':
        books = books.order_by(order_by)
    if on_sale:
        books = books.filter(discount__gt=0)

    paginator = Paginator(books, 3)
    current_page = paginator.get_page(page_number)

    return render(
        request,
        'books/books.html',
        {'page_obj': current_page}
    )

def detail(request, slug_name):
    book = get_object_or_404(Book, slug=slug_name)
    return render(
        request,
        'books/detail.html',
        {'book': book}
    )