from django.forms import ModelForm

from gallery.models import PresentationCard


class ImageForm(ModelForm):
    class Meta:
        model = PresentationCard
        fields = ["title", "description", "featured_image"]
