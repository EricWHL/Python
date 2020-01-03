# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.http import Http404
from models import Todo


def todolist(request):
    todo = Todo.objects.filter(flag=1)
    finishtodos = Todo.objects.filter(flag=0)
    return render(request, 'TodoList.html', {'todolist': todo, 'finishtodos': finishtodos})


def todofinish(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '1':
        todo.flag = '0'
        todo.save()
        return HttpResponseRedirect('/TodoList/')
    todolist = Todo.objects.filter(flag=1)
    return render(request,'TodoList.html', {'todolist': todoList})


def todoback(request, id=''):
    todo = Todo.objects.get(id=id)
    if todo.flag == '0':
        todo.flag = '1'
        todo.save()
        return HttpResponseRedirect('/TodoList/')
    todolist = Todo.objects.filter(flag=1)
    return render(request,'TodoList.html', {'todolist': todolist})


def tododelete(request, id=''):
    try:
        todo = Todo.objects.get(id=id)
    except Exception:
        raise Http404
    if todo:
        todo.delete()
        return HttpResponseRedirect('/TodoList/')
    todolist = Todo.objects.filter(flag=1)
    return render(request, 'TodoList.html', {'todolist': todolist})


def addtodo(request):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'showtodo.html', {'todolist': todolist, 'finishtodos': finishtodos})
    else:
        todolist = Todo.objects.filter(flag=1)
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'TodoList.html', {'todolist': todolist, 'finishtodos': finishtodos})


def updatetodo(request, id=''):
    if request.method == 'POST':
        atodo = request.POST['todo']
        priority = request.POST['priority']
        user = User.objects.get(id='1')
        todo = Todo(user=user, todo=atodo, priority=priority, flag='1')
        todo.save()
        todolist = Todo.objects.filter(flag='1')
        finishtodos = Todo.objects.filter(flag=0)
        return render(request, 'TodoList.html', {'todolist': todolist, 'finishtodos': finishtodos})
    else:
        try:
            todo = Todo.objects.get(id=id)
        except Exception:
            raise Http404
        return render(request, 'updatatodo.html', {'todo': todo})
