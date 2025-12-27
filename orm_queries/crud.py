from .models import *
def create_record():
    book= books(
        title="Django for Beginners",
        author=Author.objects.get(name="train"),
        published_date="2021-01-01",
        isbn="9781735467207")
    book.save()
    return None
def create_author():
    author = Author(name="saravam", email="sarvam@g.com")
    author.save()
    return None

def update_record():
    book = books.objects.get(title="Django for Beginners")
    book.title = "Django for Advanced"
    book.save()
    return None

def delete_record():
    book = books.objects.get(title="Django for Advanced")
    book.delete()
    return None

def get_all_books():
    return books.objects.all()

def get_all_authors():
    return Author.objects.all()

