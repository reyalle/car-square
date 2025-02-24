from rest_framework import generics
from .models import Car
from .serializers import CarSerializer

class CarListCreate(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarDetail(generics.ListCreateAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
