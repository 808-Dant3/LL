from django.urls import path, include
from .views import *

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', menuview.as_view()),
]