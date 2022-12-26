from rest_framework import serializers
from .models import Steps

class StepSerializer(serializers.ModelSerializer):
    """
        Steps Serializer
    """

    class Meta:
        model = Steps
        fields = "__all__"