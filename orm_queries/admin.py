from django.contrib import admin
from .models import books
# Register your models here.

@admin.register(books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'isbn')
    search_fields = ('title', 'author')
    list_filter = ('published_date',)
    ordering = ('-published_date',) # Order by published date descending
    list_display_links = ('title', 'author') # Make title and author clickable links in the admin list view