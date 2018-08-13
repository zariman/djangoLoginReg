from django.shortcuts import render, redirect, reverse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    pass