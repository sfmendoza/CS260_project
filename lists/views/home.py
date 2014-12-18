__author__ = 'sieg'

from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from lists.forms import *
from django.template import RequestContext
from django.shortcuts import render_to_response


def main_page(request):
    if 'user_id' in request.session:
        user_obj = User.objects.filter(id=request.session['user_id'])
        todo_obj = Todo.objects.filter(user_id=request.session['user_id'], status='Active')
        complete_todo_obj = Todo.objects.filter(user_id=request.session['user_id'], status='Completed')
        cancel_todo_obj = Todo.objects.filter(user_id=request.session['user_id'], status='Cancelled')
        data = RequestContext(request, {'fname': request.session['fname'],
                                        'username': request.session['username'],
                                        'user': user_obj,
                                        'todo': todo_obj,
                                        'done_tasks': complete_todo_obj,
                                        'cancel_tasks': cancel_todo_obj,
                                        'a': 0}
                              )
        return render_to_response('home.html', data)
    else:
        form = SignupForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('index.html', variables)


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.id
            request.session['user_id'] = id
            request.session['fname'] = form.cleaned_data['first_name']
            request.session['username'] = form.cleaned_data['username']
    return HttpResponseRedirect('/')


def login_user(request):
    user_obj = User.objects.filter(username=request.POST.get('username'), password=request.POST.get('password'))
    if user_obj.count():
        request.session['user_id'] = user_obj[0].id
        request.session['fname'] = user_obj[0].first_name
        request.session['username'] = user_obj[0].username
        return HttpResponseRedirect('/')
    else:
        data = {}
        return render_to_response('login.html', data)


def logout(request):
    del request.session['user_id']
    del request.session['fname']
    del request.session['username']
    request.session.modified = True
    return HttpResponseRedirect('/')


def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html', {'form': SignupForm()})


def update(request):
    return render(request, 'user_page.html', {'form': SignupForm()})
