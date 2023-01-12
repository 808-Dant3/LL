from rest_framework.decorators import api_view, permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from django.contrib.auth.models import User, Group
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import menu, booking


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

@api_view(['GET', 'POST', 'DELETE'])
class userview(APIView):
    def usersview(self, request, id):
        if request.method == 'POST':
            serialized_item = userSerializer(data = request.data)
            serialized_item.is_valid(raise_exception=True)
            serialized_item.save()
            return Response(serialized_item.validated_data,status.HTTP_201_CREATED)
        elif request.method == 'GET':
            permission_classes = [IsAuthenticated]
            users = User.objects.get()
            serialized_item = userSerializer(users, many=True)
            return Response(serialized_item.data)
        elif request.method == 'DELETE':
            users = get_object_or_404(User, id=id)
            users.delete()
            return Response({"messege": "user has been delete" })

def index(request):
    return(render(request, 'index.html'))