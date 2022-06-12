from django.forms import ModelForm
from .models import PresentationCard


class ImageForm(ModelForm):
    class Meta:
        model = PresentationCard
        fields = ["title", "description", "featured_image"]
