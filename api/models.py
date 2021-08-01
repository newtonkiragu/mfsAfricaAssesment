import uuid
from django.db import models


# Create your models here.
class Points(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    string_of_csv = models.TextField(max_length=500)
    closest_point = models.CharField(max_length=100, default="(0,0)")

    @staticmethod
    def closest_points(points):
        k = 2
        points.sort(key=lambda K: K[0] ** 2 + K[1] ** 2)
        return points[:k]


# class FormattedPoints(models.Model):
#     pass
