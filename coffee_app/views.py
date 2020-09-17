from rest_framework.response import Response
from rest_framework import status, generics
from .serializers import CoffeeMachineSerializer, CoffeePodSerializer

class CoffeeView(generics.ListAPIView):
    """
    This Class handles retreiving data from Coffee Machines & Coffee Pods models
    """
    serializer_classes = {"machines":CoffeeMachineSerializer, "pods":CoffeePodSerializer}

    def get_serializer_class(self):
        """
        return a serializer based on the screen (endpoint)
        """
        return self.serializer_classes[self.kwargs.get("TYPE")]

    def get_queryset(self):
        """
        Filter with the corresponding attributes from query paramateres
        """
        new_query = {key:self.request.query_params.get(key) for key in self.request.query_params} # this line to convert the values of the return object of query param from list of string to string
        queryset = self.get_serializer_class().Meta.model.objects.filter(**new_query)
        return queryset
