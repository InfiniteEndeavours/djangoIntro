from django.shortcuts import render, redirect, get_object_or_404
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


def edit_item(request, item_id):
    if request.method == "POST":
        # Create a new instance of the ItemForm class
        # and pass in the request.POST data
        # This will create a new form with the data that was submitted
        # in the POST request
        item = get_object_or_404(Item, id=item_id)
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')
    item = get_object_or_404(Item, id=item_id)
    form = ItemForm(instance=item)
    context = {
        'form': form
    }
    return render(request, 'todo/edit_item.html', context)
