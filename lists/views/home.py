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
        todo_obj = Todo.objects.filter(user_id=request.session['user_id'])
        data = RequestContext(request, {'fname': request.session['fname'], 'user': user_obj, 'todo': todo_obj, 'a': 0})
        return render_to_response('home.html', data)
    else:
        form = RegistrationForm()
        variables = RequestContext(request, {'form': form})
        return render_to_response('index.html', variables)


def register_page(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(fname=form.cleaned_data['fname'],
                                            lname=form.cleaned_data['lname'],
                                            password=form.cleaned_data['password1'],
                                            email=form.cleaned_data['email'])
            return HttpResponseRedirect('/')
    form = RegistrationForm()
    variables = RequestContext(request, {'form': form})
    return render_to_response('registration/register.html', variables)


def signup(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            obj = form.save()
            id = obj.id
            request.session['user_id'] = id
            request.session['fname'] = form.cleaned_data['fname']
    return HttpResponseRedirect('/')


def login(request):
    user_obj = User.objects.filter(email=request.POST.get('email'), password=request.POST.get('password'))
    if user_obj.count():
        print
        user_obj
        request.session['user_id'] = user_obj[0].id
        request.session['fname'] = user_obj[0].fname
    return HttpResponseRedirect('/')


def logout(request):
    del request.session['user_id']
    del request.session['fname']
    request.session.modified = True
    return HttpResponseRedirect('/')