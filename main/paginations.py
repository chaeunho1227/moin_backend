from rest_framework.pagination import PageNumberPagination

class AiPagination(PageNumberPagination):
    page_size = 12

class AiCommentListPagination(PageNumberPagination):
    page_size = 10