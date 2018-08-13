from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib import messages

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'semi_restful/index.html', context)

def new(request):
    return render(request, 'semi_restful/new.html')

def create(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request,value)
            return redirect(reverse('my_new'))
        else:
            form = request.POST
            User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'])

    return redirect('/users/new')

def show(request, id):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'semi_restful/show.html', context)

def edit(request, id):
    context = {
        'user': User.objects.get(id=id)
    }    
    return render(request, 'semi_restful/edit.html', context)

def update(request):
    if request.method == 'POST':
        form = request.POST
        errors = User.objects.basic_validator(request.POST)

        if len(errors):
            for key, value in errors.items():
                messages.error(request,value)
            return redirect(reverse('my_edit', kwargs = {'id': form['id']}))
        else:
            user_update = User.objects.get(id=form['id'])
            user_update.first_name = form['first_name']
            user_update.last_name = form['last_name']
            user_update.email = form['email']
            user_update.save()

    return redirect(reverse('my_edit', kwargs = {'id': form['id']}))

def destroy(request, id):
    User.objects.get(id=id).delete()
    return redirect(reverse('my_index'))



