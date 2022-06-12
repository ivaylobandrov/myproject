from rest_framework import serializers
from .models import PresentationCard


class PresentationCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationCard
        fields = "__all__"
