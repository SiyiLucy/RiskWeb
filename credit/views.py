from django.shortcuts import render

def credit_view(request):
    return render(request, 'credit.html')
