from rest_framework.validators import UniqueTogetherValidator
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = booking
        fields = ['id', 'name', 'no_of_guests', 'bookingDate']

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = menu
        fields = ['id', 'title', 'price', 'inventory']
