from django.shortcuts import render

def index(request):
    return render(request, 'credit_app/index.html')  # 确保路径正确
