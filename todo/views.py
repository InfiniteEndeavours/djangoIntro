from django.shortcuts import render
from .models import Item


# Create your views here.

# Create a view that will return a list of to do items
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


# Create a view to add an item to the Todo List
def add_item(request):
    return render(request, 'todo/add_item.html')