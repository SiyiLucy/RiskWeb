# project/views.py (项目根目录)
from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
