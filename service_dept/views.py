from rest_framework import generics
from .models import ServiceAppointment
from .serializers import AppointmentSerializer

class ServiceAppointmentCreate(generics.ListCreateAPIView):
    queryset = ServiceAppointment.objects.all()
    serializer_class = AppointmentSerializer

class ServiceAppointmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServiceAppointment.objects.all()
    serializer_class = AppointmentSerializer
