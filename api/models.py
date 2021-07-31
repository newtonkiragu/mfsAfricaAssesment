import uuid
from django.db import models


# Create your models here.
class Points(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    string_of_csv = models.TextField(max_length=500)
    closest_point = models.CharField(max_length=100, default="(0,0)")


# class FormattedPoints(models.Model):
#     pass
