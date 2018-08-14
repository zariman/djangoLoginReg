from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages
from ..login_reg.models import User
from .models import Message, Comment
import datetime

def wall(request):
    if not 'user_id' in request.session:
        return redirect('/')

    user = User.objects.get(id=request.session['user_id'])
    context = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'created_at': user.created_at,
        'updated_at': user.updated_at,
        'texts': Message.objects.order_by("-created_at").all(),
    }

    return render(request,'the_wall/wall.html', context)


def logout(request):
    request.session.flush()

    return redirect('/')

def message(request):
    if request.method == 'POST':
        form = request.POST
        Message.objects.create(user=User.objects.get(id=request.session['user_id']), message=form['message'])
    
    return redirect('/wall')

def comment(request):
    if request.method == 'POST':
        form = request.POST
        print(form['message_id'])
        Comment.objects.create(user=User.objects.get(id=request.session['user_id']), message=Message.objects.get(id=form['message_id']), comment=form['comment']) 

    return redirect('/wall')

def delete(request):
    #TODO: implement deleting messages
    if request.method == 'POST':
        form = request.POST
        time = Message.objects.get(id=form['message_id']).created_at.replace(tzinfo = None)
        if (int)(((datetime.datetime.utcnow() - time).total_seconds())/60) < 30.0: 
            Message.objects.get(id=form['message_id']).delete()
        else:
            messages.error(request, "Cannot delete messages older than 30 minutes", int(form['message_id']))

    return redirect('/wall')
