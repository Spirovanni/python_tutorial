from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Book
from django.shortcuts import render

# Create your views here.
# class Another(View):
#
#     book = Book.objects.get(id=4)
#     output = f"We have {book.title} book with ID {book.id} in DB and it has a price of {book.price}<br>"

    # for book in books:
    #     output += f"We have {book.title} book with ID {book.id} in DB and it has a price of {book.price}<br>"

    # def get(self, request):
    #     return HttpResponse(self.output)

def first(request):
    return render(request, 'first_temp.html')
