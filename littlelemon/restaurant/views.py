from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *


class menuview(APIView):
    def get(self, request):
        items = menu.objects.all()
        serializers = bookingSerializer(items, many=True)
        return Response(serializers.data)

class bookingview(APIView):
    def get(self, request):
        items = booking.objects.all()
        serializers = menuSerializer(items, many=True)
        return Response(serializers.data)

class BookingView(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

class MenuItemView(generics.ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = User.objects.all()
   serializer_class = userSerializer
   permission_classes = [IsAuthenticated] 

def index(request):
    return(render(request, 'index.html'))