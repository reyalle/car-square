from rest_framework import serializers
from .models import ServiceAppointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceAppointment
        fields = "__all__"
