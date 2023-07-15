from django.shortcuts import render, redirect
from .models import Book


def book_list(request):
    query = request.GET.get('q')

    if query:
        books = Book.objects.filter(title__icontains=query) | Book.objects.filter(genre__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'book_manager/book_list.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        genre = request.POST['genre']
        height = request.POST['height']
        publisher = request.POST['publisher']
        Book.objects.create(title=title, author=author, genre=genre, height=height, publisher=publisher)
        return redirect('book_list')
    return render(request, 'book_manager/add_book.html')


def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST['title']
        book.author = request.POST['author']
        book.genre = request.POST['genre']
        book.height = request.POST['height']
        book.publisher = request.POST['publisher']
        book.save()
        return redirect('book_list')
    return render(request, 'book_manager/edit_book.html', {'book': book})


def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
