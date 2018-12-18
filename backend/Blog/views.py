from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status

from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication

from django.contrib.auth import get_user_model

from .models import Article, Comment, Category
from .serializers import ArticlesSerializer, CommentsSerializer, CategorysSerializer


User = get_user_model()

class BasePagination(PageNumberPagination):
    """
    分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


class ArticlesViewset(mixins.ListModelMixin, mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin, viewsets.GenericViewSet, ):
    """
    文章:
        列表
        详情
    """
    queryset = Article.objects.all()
    serializer_class = ArticlesSerializer
    pagination_class = BasePagination
    filter_backends = (filters.OrderingFilter, filters.SearchFilter,)
    ordering_fields = ('created', 'views')
    search_fields = ('category__text', 'title', 'author__username', )

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        # 统计文章阅读量
        instance.increase_views()
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        user_name = self.request.user
        user = User.objects.get(username=user_name)
        user.increase_point()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class CommentsViewset(mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    评论:
        列表
        详情
        创建
    """
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    pagination_class = BasePagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('article__id',)


class CategorysViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    种类:
        列表
        详情
    """
    queryset = Category.objects.all()
    serializer_class = CategorysSerializer
    pagination_class = BasePagination
    ordering_fields = ('created', 'views')
    search_fields = ('category__id')
