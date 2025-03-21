from rest_framework.pagination import LimitOffsetPagination

class CustomLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 100
    max_limit = 1000
    limit_query_param = 'limit'
    offset_query_param = 'offset'