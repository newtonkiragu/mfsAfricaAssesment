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
        response = self.client.get(reverse('point', kwargs={'pk': point.id}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, point)

    def test_update_point(self):
        point_id = 1
        self.new_set_of_points.save()
        point = models.Points.objects.get(pk=point_id)
        change_point = {'code': 'return False'}
        res = self.client.put(
            reverse('point', kwargs={'pk': point.id}),
            change_point, format='json'
        )
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_delete_point(self):
        point_id = 1
        # self.new_set_of_points.save()
        point = models.Points.objects.get(pk=point_id)
        response = self.client.delete(
            reverse('point', kwargs={'pk': point.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
