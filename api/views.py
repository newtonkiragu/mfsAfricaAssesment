from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from api.models import Points
from api.serializers import PointsSerializer


class PointsViewSets(viewsets.ModelViewSet):
    """
        API endpoint that allows points to be viewed
    """
    queryset = Points.objects.all()
    serializer_class = PointsSerializer
