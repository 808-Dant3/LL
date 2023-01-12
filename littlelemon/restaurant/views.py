from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from django.shortcuts import render
from .serializers import *
from .models import *


class menuview(APIView):
    def get(self, request):
        items = menu.objects.all()
        serializers = bookingSerializer(items, many=True)
        return Response(serializers.data)

def index(request):
    return(render(request, 'index.html'))