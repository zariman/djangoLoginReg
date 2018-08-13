from django.shortcuts import render, redirect, reverse, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'login_reg/index.html')

def register(request):
    if request.method == 'POST':
        form = request.POST
        hash1 = bcrypt.hashpw(form['password'].encode(), bcrypt.gensalt())
        errors = User.objects.basic_validator(form)
        
        if len(errors):
            for key, value in errors.items():
                messages.error(request,value)

            print(errors)
            return redirect(reverse('login_reg:my_index'))
        else:
            user = User.objects.create(first_name=form['first_name'], last_name=form['last_name'], email=form['email'], password=hash1)
            print(user.id)
            request.session['user_id'] = User.objects.get(email=form['email']).id
            return redirect(reverse('the_wall:wall'))

def login(request):
    if request.method == 'POST':
        form = request.POST
        
        errors = User.objects.basic_validator2(form)
        print("Length of errors:",len(errors))
        if len(errors):
            for key, value in errors.items():
                messages.info(request,value)
            return redirect(reverse('login_reg:my_index'))
        else:
            request.session['user_id'] = User.objects.get(email=form['email']).id
            return redirect(reverse('the_wall:wall'))

        return redirect('/')

def wall(request):
    return render(request, 'the_wall/wall.html')
