from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm


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
        # Create a new instance of the ItemForm class
        # and pass in the request.POST data
        # This will create a new form with the data that was submitted
        # in the POST request
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)
