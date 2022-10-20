from rest_framework import serializers
from main.models import Workers

class WorkersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Worker
        fields('pk', 'first_name', 'last_name', 'email', 'phone', 'address', 'description')
