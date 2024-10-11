from rest_framework import serializers
from .models import *

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apps
        fields = '__all__'