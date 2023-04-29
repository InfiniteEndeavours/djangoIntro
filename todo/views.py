from django.shortcuts import render


# Create your views here.

# Create a view that will return a list of to do items
def get_todo_list(request):
    return render(request, 'todo/todo_list.html')
