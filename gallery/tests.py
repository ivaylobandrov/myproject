"""
Tests for Gallery APIs.
"""
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from gallery.models import PresentationCard

GALLERY_URL = reverse('cards_api')


def detail_url(card_id):
    """Create and return an card detail URL."""
    return reverse('card_api', args=[card_id])


class PublicGalleryAPITests(TestCase):
    """Test Gallery API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_list_cards(self):
        """Test list cards."""
        PresentationCard.objects.create(title='first title', description="description")
        PresentationCard.objects.create(title='second title', description="second description")
        response = self.client.get(GALLERY_URL)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_card(self):
        """Test retrieve a card."""
        card = PresentationCard.objects.create(title='first title', description="description")
        url = detail_url(card.id)
        response = self.client.get(url)
        print("RESPONSE", response.json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)
