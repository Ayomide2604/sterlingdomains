from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title']


@admin.register(Domain)
class DomainAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_sold', 'price', 'category', 'add_date']
    list_display_links = ['id', 'title']
    list_editable = ['price', 'is_sold']
    list_per_page = 25
    list_filter = ['category']
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ['title']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone',
                    'offer', 'message', 'contact_date']
