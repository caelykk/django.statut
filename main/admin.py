from django.contrib import admin
from .models import Author, Book

# Register your models here.


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	prepopulated_fields = {"url": ("name", "last_name")}

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	prepopulated_fields = {"url": ("title",)}