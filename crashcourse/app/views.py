from django.shortcuts import render
from app.models import Task

def index(request):
    task_list = Task.objects.all()
    return render(request, 'app/index.html', {'tasks': task_list})
