from typing import Any
from django.shortcuts import render
from django.views.generic import View
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.views.generic import ListView
from myapp.models import BookModel

# Create your views here.

# Normal Class based View without templates
class ClassView(View):
    def get(self, request):
        return HttpResponse('<h1>This is Class Test message </h1>')


# Class Based View With Templates
class TemplateBaedView(TemplateView):
    template_name = 'myapp/home.html'
    
    
# Templates based class view including context data
class TemplatesContextView(TemplateView):
    template_name = 'myapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['testmsg'] = 'This is test message'
        context['title'] = 'Title is Test'
        return context
    

# class BookListView(ListView):
#     model = BookModel
#     # Default template file : bookmodel_list.html
#     template_name = 'myapp/home.html'
#      # Default context Object name : bookmodel_list
#     context_object_name = 'books'


class BookListView(ListView):
    model = BookModel