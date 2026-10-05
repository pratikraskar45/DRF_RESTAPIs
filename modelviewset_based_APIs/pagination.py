from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CustomPagination(PageNumberPagination):

    # Default records per page
    page_size = 5

    # URL parameter for page number
    page_query_param = 'page'

    # Allow user to change page size
    page_size_query_param = 'page_size'

    # Maximum records user can request
    max_page_size = 10

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'page': self.page.number,
            'page_size': self.get_page_size(self.request),
            'total_pages': self.page.paginator.num_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })