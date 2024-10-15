from django.contrib import admin
from myapp.models import BookModel

# Register your models here.

class BookModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'pages', 'price']


admin.site.register(BookModel, BookModelAdmin)