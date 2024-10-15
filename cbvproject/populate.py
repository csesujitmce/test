import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cbvproject.settings')

import django
django.setup()

from faker import Faker
from random import *
from myapp2.models import Book

fakegen= Faker()

def populate(n):
    for i in range(n):
        ftitle = fakegen.name()
        fauthor = fakegen.name()
        fpages = fakegen.random_int(100, 500)
        fprice = fakegen.random_int(500, 2000)
        book_record = Book.objects.get_or_create(title=ftitle, author=fauthor, pages=fpages, price=fprice)
        
n = int(input("Create a number want to insert data : "))   
populate(n)
print("{} Data Inserted Sucessfully".format(n))
