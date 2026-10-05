from rest_framework import viewsets, status, filters
from rest_framework.response import Response

from modelviewset_based_APIs.models import Vehicle
from modelviewset_based_APIs.pagination import CustomPagination
from modelviewset_based_APIs.serializers import VehicleSerializer


class VehicleModelViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    # Pagination
    pagination_class = CustomPagination

    # Filters
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    # Fields where search is allowed
    search_fields = [
        'vehicle_number',
        'owner_name',
        'owner_email',
        'phone',
        'vehicle_type',
        'brand',
        'model_name'
    ]

    # Fields where ordering is allowed
    ordering_fields = [
        'vehicle_number',
        'owner_name',
        'manufacturing_year',
        'price',
        'registration_date'
    ]

    # Default ordering
    # ordering = ['vehicle_number']