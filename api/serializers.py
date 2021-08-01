from rest_framework import serializers
from api.models import Points


class PointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Points
        fields = ['id', 'string_of_csv', 'closest_point']
