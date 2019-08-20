from .models import *
from rest_framework import serializers

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Games
        fields = ('id','title','platform','score','genre','editors_choice')
