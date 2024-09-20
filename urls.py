# credit/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.credit_view, name='credit'),
]
