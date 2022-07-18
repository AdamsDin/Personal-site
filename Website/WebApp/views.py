from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    return render(request, 'WebApp/Main.html')


def cont(request):
    task = Task.objects.all()
    return render(request, 'WebApp/Contacts.html', {'title': 'Social network', 'tasks': 'title'})





