from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'tasks/home.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm()
    return render(request, 'tasks/add_task.html', {'form': form})

def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.delete()
    return redirect('task_list')
