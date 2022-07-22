from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import Taskform


def index(request):
    return render(request, 'WebApp/Main.html')


def cont(request):
    error = ''
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Error. The form is incorrect'
    tasks = Task.objects.all()
    form = Taskform()
    context = {
        "tasks": tasks,
        "form": form,
        "error": error
    }
    return render(request, 'WebApp/Contacts.html', context)





