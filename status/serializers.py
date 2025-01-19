from rest_framework import serializers
from status.models import Status

class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = ['id', 'text', 'created_at', 'user']