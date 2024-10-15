from django.urls import path
from myapp2 import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='home'),
    path('<int:pk>', views.BookDetailsView.as_view(), name='detail'),
    path('create/', views.BookCreateView.as_view()),
]
