from django.shortcuts import render
from app.models import Category

def index(request):
    category_list = Category.objects.all()
    return render(request, 'app/index.html', {'categories': category_list})
