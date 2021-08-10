import uuid
from django.db import models


# Create your models here.
class Points(models.Model):
    """Model for Points class"""
    string_of_csv = models.TextField(max_length=500)
    closest_point = models.CharField(max_length=100, default="(0,0)")

    @staticmethod
    def closest_points(points):
        """find the set of points closest to zero

        :param points:
        :type points: str
        :return computed list of comma separated values sorting them from the point nearest zero:
        :rtype list:
        """

        k = 2
        points.sort(key=lambda K: K[0] ** 2 + K[1] ** 2)
        return points[:k]

# loop through the list of points
# get a specific pair of points
# compare the set of points to the previous set
# splice the list created to get the closest points

