from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import TodoItem

def todoView(request):
    all_todo_items = TodoItem.objects.all()
    return render(request,'todo.html',
    {'all_items':all_todo_items})


def addTodo(request):
    #create new todo item
    c = request.POST['content']
    #save the item database
    new_item = TodoItem (content = c)
    new_item.save()
    return HttpResponseRedirect('/pollstest/')
    #redirect to browser
