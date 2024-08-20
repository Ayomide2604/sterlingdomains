from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Domain(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=True)
    is_sold = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    url = models.URLField(max_length=200)
    description = models.TextField(blank=True, null=True)
    add_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='employee/photos/%Y/%m/%d/')
    email = models.EmailField()
    job_title = models.CharField(max_length=200, null=True)
    is_mvp = models.BooleanField(default=False)
    add_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        full_name = f'{self.first_name} {self.last_name}'
        return full_name


class Contact(models.Model):
    domain = models.CharField(max_length=200, null=True, blank=True)
    domain_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100, blank=True, null=True)
    offer = models.PositiveIntegerField(blank=True, null=True)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
