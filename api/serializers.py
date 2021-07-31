from rest_framework import serializers

from api.models import Points


class PointsSerializer(serializers.Serializer):
    class Meta:
        model = Points
        fields = ['string_of_csv', 'closest_point']
