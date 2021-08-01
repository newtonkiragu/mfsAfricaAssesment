import uuid
from django.db import models


# Create your models here.
class Points(models.Model):
    string_of_csv = models.TextField(max_length=500)
    closest_point = models.CharField(max_length=100, default="(0,0)")

    @staticmethod
    def closest_points(points):
        sorting_dictionary = {}

        for x in points:
            p = x[0] - x[1]
            sorting_dictionary[x] = p

        computed_list = list({k: v for k, v in
                              sorted(sorting_dictionary.items(), key=lambda item: item[1], reverse=True)}.keys())
        print(computed_list)
        return computed_list
