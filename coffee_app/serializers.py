from rest_framework import serializers
from .models import CoffeeMachines, CoffeePods

class CoffeePodSerializer(serializers.ModelSerializer):
    """
    Model serializer class for CoffeePods model data
    """
    class Meta:
        model = CoffeePods
        fields = ["code"]

class CoffeeMachineSerializer(serializers.ModelSerializer):
    """
    Model serializer class for CoffeeMachines model data
    """
    class Meta:
        model = CoffeeMachines
        fields = ["code"]