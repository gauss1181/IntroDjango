from django.shortcuts import render
from app.models import Task
from app.forms import TaskForm

def index(request):
    task_list = Task.objects.all()
    return render(request, 'app/index.html', {'tasks': task_list})

def about(request):
    return render(request, 'app/about.html')

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = TaskForm()
    return render(request, 'app/add_task.html', {'form': form})
