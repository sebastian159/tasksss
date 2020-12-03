from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Tasks, models


# Create your views here.
def index(request):
    task = Tasks.objects.all()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm()

    context = {'tasks': task, 'form': form}
    return render(request, 'tasks/index.html', context)


def update(request, id):
    task = Tasks.objects.get(id=id)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
    else:
        form = TaskForm(instance=task)

    context = {'form': form}
    return render(request, 'tasks/update.html', context)


def delete(request, id):
    task = Tasks.objects.get(id=id)
    if request.method == 'POST':
        task.delete()
        return redirect('index')
    context = {'tasks': task}
    return render(request, 'tasks/delete.html', context)


def complete(request, id):
    task = Tasks.objects.get(id=id)
    task.created_at = True
    return redirect('index')