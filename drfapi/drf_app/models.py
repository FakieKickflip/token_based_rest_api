from typing_extensions import Required
from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Author(models.Model):
    first_name = models.CharField(max_length=250) 
    last_name = models.CharField(max_length=250)
    date_of_birth = models.DateField(default=datetime.date(1999,12,12))
    created_at = models.DateTimeField(blank=True, default=timezone.now) 
    updated_at = models.DateTimeField(blank=True, auto_now=True)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name    


class Article(models.Model):
    title = models.CharField(max_length=250) #this field is required via Serailizer
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, default=timezone.now) 
    updated_at = models.DateTimeField(blank=True, auto_now=True) #date, when the objects gets updated

    def __str__(self) -> str:
        return self.title


