from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import Taskform


def index(request):
    return render(request, 'WebApp/Main.html')


def cont(request):
    tasks = Task.objects.all()
    form = Taskform()
    context = {
        "tasks": tasks,
        "form": form
    }
    return render(request, 'WebApp/Contacts.html', context)





