from django.shortcuts import render
from django.http import HttpResponse
from .models import Task


def index(request):
    return render(request, 'WebApp/Main.html')


def cont(request):
    tasks = Task.objects.all()
    context = {
        "tasks": tasks
    }
    return render(request, 'WebApp/Contacts.html', context)





