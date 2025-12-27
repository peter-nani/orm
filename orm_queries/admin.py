from django.contrib import admin
from .models import books, Author
# Register your models here.

@admin.register(books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    ordering = ('-published_date',) # Order by published date descending
    list_display_links = ('title', 'author') # Make title and author clickable links in the admin list view

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')
    ordering = ('name',)
    list_display_links = ('name',) # Make name clickable link in the admin list view
    list_filter = ('name',) # Filter by author name in the admin list view 
