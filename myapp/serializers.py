from rest_framework import serializers
from .models import Textsearch,ImageSearch

class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Textsearch
        fields = "__all__"


class Imageserializer(serializers.ModelSerializer):
    class Meta:
        model = ImageSearch
        fields= "__all__"