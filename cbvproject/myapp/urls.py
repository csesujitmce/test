from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.ClassView.as_view()),
    path('temp', views.TemplateBaedView.as_view()),
    path('tt', views.TemplatesContextView.as_view()),
    path('book/', views.BookListView.as_view()),
]
