from django.urls import path
from .views import ServiceAppointmentCreate, ServiceAppointmentDetail

urlpatterns = [
    path("service/", ServiceAppointmentCreate.as_view(), name="service-list"),
    path("service/<int:pk>/", ServiceAppointmentDetail.as_view(), name="service-detail"),
]
