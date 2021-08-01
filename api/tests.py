from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from . import models


class PointsTestCase(APITestCase):

    def setUp(self):
        self.new_set_of_points = models.Points(1, "(2,3), (1,1), (5, 4)")

    def test_view_points(self):
        old_count = models.Points.objects.count()
        self.new_set_of_points.save()
        new_count = models.Points.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_view_point(self):
        point_id = 1
        self.new_set_of_points.save()
        point = models.Points.objects.get(pk=point_id)
        response = self.client.get(reverse('points', kwargs={'pk': point.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, point)
