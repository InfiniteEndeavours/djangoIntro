from django.shortcuts import render, redirect
from .models import Item


# Create your views here.

# Create a view that will return a list of to do items
def get_todo_list(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


# Create a view to add an item to the to do List
def add_item(request):
    if request.method == "POST":
        name = request.POST.get('item_name')
        done = 'done' in request.POST
        Item.objects.create(name=name, done=done)

        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
