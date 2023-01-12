from django.urls import path, include
from .views import *

urlpatterns = [
    ##path('menu/', menuview.as_view()),
    path('', MenuItemView.as_view()),
    path('<int:pk>', SingleMenuItemView.as_view()),
    path('booking', bookingview.as_view()),
]