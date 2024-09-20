from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='credit'),  # 将其命名为 'credit'
]
