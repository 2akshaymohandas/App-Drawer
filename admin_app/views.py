from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import status



@api_view(['GET'])
def Apps_details(request):
    apps = Apps.objects.all()
    serializer = TaskSerializer(apps, many=True)

    return Response(serializer.data)