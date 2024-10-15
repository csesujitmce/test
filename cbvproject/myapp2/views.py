from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView
from myapp2.models import Book

class BookListView(ListView):
    model = Book
    


# Create your views here.
class BookDetailsView(DetailView):
    model = Book
    # default template file name modelname_detail.html i.e. book_detail.html
    #  default context object or modelname   
    # 

class BookCreateView(CreateView)  :
    model=Book
    fields = ('title', 'author', 'pages', 'price') 