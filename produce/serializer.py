# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     serializer
   Description :
   Author :       Administrator
   date：          2019/3/29 0029
-------------------------------------------------
   Change Activity:
                   2019/3/29 0029:
-------------------------------------------------
"""
from rest_framework import serializers
from .models import TypeModel, TypeContent


class ContentSerializers(serializers.ModelSerializer):
    class Meta:
        model = TypeContent
        fields = '__all__'


class TypeSerializers(serializers.ModelSerializer):
    contents = ContentSerializers(many=True)

    class Meta:
        model = TypeModel
        fields = '__all__'
