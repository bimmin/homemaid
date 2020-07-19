from rest_framework import serializers

from .models import Maid

class MaidSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maid
        fields = ('id', 'name',)