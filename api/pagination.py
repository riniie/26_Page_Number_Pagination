from rest_framework.pagination import PageNumberPagination


class CustomPageNumberPagination(PageNumberPagination):
    page_size = 1
    page_query_param = 'next'
    page_size_query_param = 'record'
    max_page_size = 2
    last_page_strings = 'end'
