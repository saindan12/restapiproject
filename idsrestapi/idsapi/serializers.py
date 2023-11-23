
from rest_framework import serializers
from .models import Network

class NetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Network
        fields = ['timestamp', 'source_ip', 'destination_ip', 'protocol']
