__author__ = 'sieg'


from django.http import HttpResponseRedirect
from lists.forms import *
from lists.models import *
from django.template import RequestContext
from django.shortcuts import render_to_response

def add_todo(request):
    if request.method == 'POST':
        todo_obj = Todo(todo_job=request.POST.get('job'), user_id=request.session['user_id'])
        todo_obj.save()
        return HttpResponseRedirect('/')
    else:
        data = RequestContext(request, {'username': request.session['username']})
        return render_to_response('add_todo.html', data)

def edit_todo(request, todo_id):
    if request.method == 'POST':
        todo_obj = Todo.objects.filter(id=request.POST.get('id')).update(todo_job=request.POST.get('job'))
        return HttpResponseRedirect('/')
    else:
        todo_obj = Todo.objects.filter(id=todo_id)
        data = RequestContext(request, {'username': request.session['username'], 'todo': todo_obj[0]})
        return render_to_response('edit_todo.html', data)

def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    return HttpResponseRedirect('/')

def cancel_todo(request, todo_id):

        todo_obj = Todo.objects.get(id=todo_id)
        todo_obj.status = 'Cancelled'
        todo_obj.save()

        return HttpResponseRedirect('/')

def complete_todo(request, todo_id):

        todo_obj = Todo.objects.get(id=todo_id)
        todo_obj.status = 'Done'
        todo_obj.save()

        return HttpResponseRedirect('/')