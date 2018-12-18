from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, mixins
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework_jwt.serializers import jwt_encode_handler, jwt_payload_handler

from django.contrib.auth import get_user_model

from .serializers import UserProfileSerializer, UserRegisterSerializer

User = get_user_model()

class BasePagination(PageNumberPagination):
    """
    分页
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10


class UserProfileViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                        viewsets.GenericViewSet):
    """
    用户资料:
        详情
        列表
    """
    queryset = User.objects.all()
    serializer_class = UserProfileSerializer
    pagination_class = BasePagination
    lookup_field = 'username'


class UserRegisterViewset(CreateModelMixin, viewsets.GenericViewSet):
    """
    用户注册
    """
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = self.perform_create(serializer)
        re_dict = serializer.data
        payload = jwt_payload_handler(user)
        re_dict["token"] = jwt_encode_handler(payload)
        re_dict["username"] = user.username if user.username else user.username

        headers = self.get_success_headers(serializer.data)
        return Response(re_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        return serializer.save()
