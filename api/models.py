from django.db import models


# Create your models here.
class Points(models.Model):
    string_of_csv = models.CharField(max_length=500)

