from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import csv
from django.core.paginator import Paginator

from book_manager.models import Book


def read_books_from_file():
    books = []
    with open('data/books_list.txt', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            book = {
                'title': row[0],
                'author': row[1],
                'genre': row[2],
                'height': row[3],
                'publisher': row[4]
            }
            books.append(book)
    return books

def write_books_to_file(books):
    with open('data/books_list.txt', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Author', 'Genre', 'Height', 'Publisher'])
        for book in books:
            writer.writerow([book['title'], book['author'], book['genre'], book['height'], book['publisher']])

# def book_list(request):
#     query = request.GET.get('q')
#
#     if query:
#         books = [book for book in read_books_from_file() if query.lower() in book['title'].lower() or query.lower() in book['genre'].lower()]
#     else:
#         books = read_books_from_file()
#     return render(request, 'book_manager/book_list.html', {'books': books})

def book_list(request):
    query = request.GET.get('q')

    if query:
            books = [book for book in read_books_from_file() if query.lower() in book['title'].lower() or query.lower() in book['genre'].lower()]
    else:
            books = read_books_from_file()

    paginator = Paginator(books, 10)  # Show 10 books per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'book_manager/book_list.html', {'page_obj': page_obj})



def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        height = request.POST['height']
        publisher = request.POST['publisher']

        books = read_books_from_file()
        book = {
            'title': title,
            'author': author,
            'genre': genre,
            'height': height,
            'publisher': publisher
        }
        books.append(book)

        write_books_to_file(books)
        return redirect('book_list')
    return render(request, 'book_manager/add_book.html')

def edit_book(request, book_id):
    books = read_books_from_file()
    book = books[book_id-1]

    if request.method == 'POST':
        book['title'] = request.POST['title']
        book['author'] = request.POST['author']
        book['genre'] = request.POST['genre']
        book['height'] = request.POST['height']
        book['publisher'] = request.POST['publisher']

        write_books_to_file(books)
        return redirect('book_list')
    return render(request, 'book_manager/edit_book.html', {'book': book, 'book_id': book_id})

def delete_book(request, book_id):
    books = read_books_from_file()
    del books[book_id-1]
    write_books_to_file(books)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
