from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from api.models import Points
from api.serializers import PointsSerializer


class PointsViewSet(viewsets.ViewSet):
    """
    Points Viewset to display a list of points and the computed points.
    Can perform GET and POST
    """

    def list(self, request):
        queryset = Points.objects.all()
        serializer = PointsSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        points = list(eval(request.data))
        result = Points.closest_points(points)
        data = {"string_of_csv": str(points), "closest_point": str(result)}
        serializer = PointsSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        points_model = Points(**serializer.data)
        points_model.save()
        return Response({'items': result})

    def retrieve(self, request, pk=None):
        queryset = Points.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = PointsSerializer(user)
        return Response(serializer.data)
