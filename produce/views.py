from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from django.http import JsonResponse
from .serializer import TypeSerializers, ContentSerializers
from .models import *


# Create your views here.
class TypeViewSet(viewsets.ModelViewSet):
    serializer_class = TypeSerializers
    queryset = TypeModel.objects.all()


class ContentViewSet(viewsets.ModelViewSet):
    serializer_class = ContentSerializers
    queryset = TypeContent.objects.all()
