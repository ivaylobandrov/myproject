import django_filters

from gallery.models import PresentationCard


class CardFilter(django_filters.FilterSet):

    class Meta:
        model = PresentationCard
        fields = ['title']
