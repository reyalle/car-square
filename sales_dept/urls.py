from django.urls import path
from .views import SaleListCreate, SaleDetailView

urlpatterns = [
    path("sales/", SaleListCreate.as_view(), name="sales-list"),
    path("sales/<int:pk>/", SaleDetailView.as_view(), name="sale-detail"),
]
