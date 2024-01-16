from django.http import HttpResponseRedirect
from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from .models import Book,Category,Author,Wishlist,Borrowing
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required
# Create your views here.

def HomePage(request):
  
  categories = Category.objects.all()[:6]
  authors = Author.objects.all()[:6]
  books = Book.objects.all()[:8]
  context={
    'categories':categories, 
    'authors':authors,
    'books':books 
  }
  return render(request, 'index.html',context)


def BookDetailPage(request,slug):
  book = get_object_or_404(Book, slug=slug)
  related_books=Book.objects.filter(category__name=book.category).exclude(slug=book.slug)
  return render(request, 'book_detail.html',{'book':book, 'related_books':related_books})

def AllCategories(request):
  categories = Category.objects.all()
  context={
        'categories':categories
    }
  return render(request, 'all_categories.html', context)

def AllAuthor(request):
  authors = Author.objects.all()
  context={
        'authors':authors
    }
  return render(request, 'all_authors.html', context)


def AllBooks(request):
  books = Book.objects.all()


   # searching the  book
  query = request.GET.get('search')
  if query:
      books = Book.objects.filter(Q(title__contains=query) )
  else:
      books = Book.objects.all().order_by('-id')

     # pagination
  items_per_page = 8
  paginator = Paginator(books, items_per_page)
  page = request.GET.get('page')
  try:
        books = paginator.page(page)
  except PageNotAnInteger:
        books = paginator.page(1)
  except EmptyPage:
        books = paginator.page(paginator.num_pages)


  context={
        'books':books
    }
  return render(request, 'all_books.html', context)


def CategoryFilter(request,category_name):
    category = get_object_or_404(Category, name=category_name)
    books = Book.objects.filter(Q(category__name=category))
    context={
        'books':books
    }
    return render(request, 'filter_categories.html', context)


def AuthorFilter(request,author_name):
    author = get_object_or_404(Author, name=author_name)
    books = Book.objects.filter(Q(author__name=author))
    context={
        'books':books
    }
    return render(request, 'filter_auhtor.html', context)

@login_required(login_url='login')
def add_wishlist(request, pk=None):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, pk=pk)
        Wishlist.objects.get_or_create(user=request.user, book=book)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def remove_wishlist(request, pk=None):
    data = get_object_or_404(Wishlist, pk=pk)
    data.delete() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

@login_required(login_url='login')
def add_borrowing(request, pk=None):
    if request.user.is_authenticated:
        book = get_object_or_404(Book, pk=pk)
        Borrowing.objects.get_or_create(user=request.user, book=book)
        book.num_of_books_available -= 1
        book.save()
        
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )

def remove_borrowing(request, pk=None):
    data = get_object_or_404(Borrowing, pk=pk)
    data.book.num_of_books_available += 1
    data.save()
    data.delete() 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER') )


