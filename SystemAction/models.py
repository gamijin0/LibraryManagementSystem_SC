from django.db import models

# Create your models here.

class Book(models.Model):
    book_id = models.CharField(max_length=20,primary_key=True,null=False)
    book_name = models.CharField(max_length=50,null=False)
    author = models.CharField(max_length=50,null=False)
    press = models.CharField(max_length=50,null=False)
    publication_year = models.SmallIntegerField(max_length=6,null=False)
    introduction = models.CharField(max_length=1000)
    add_time = models.DateField(auto_now=True)
    category_id = models.CharField(max_length=20,null=False)
    inventory = models.SmallIntegerField(max_length=4,null=False)

