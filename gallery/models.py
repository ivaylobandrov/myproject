import uuid

from django.db import models

from user.models import User


class PresentationCard(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, unique=True, primary_key=True, editable=False
    )
    title = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    featured_image = models.ImageField(null=True, blank=True, upload_to="images/")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ["-created"]
