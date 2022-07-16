from rest_framework import serializers

from gallery.models import PresentationCard


class PresentationCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresentationCard
        fields = "__all__"
