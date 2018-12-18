from django.contrib import admin
from django.conf.urls import include
from django.urls import path, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter

from Blog.views import ArticlesViewset, CommentsViewset, CategorysViewset
from BlogUser.views import UserProfileViewset, UserRegisterViewset

router = DefaultRouter()

# 文章
router.register(r'posts', ArticlesViewset, base_name="article")
router.register(r'comments', CommentsViewset, base_name="comment")
router.register(r'categorys', CategorysViewset, base_name="category")
# 用户
router.register(r'users', UserProfileViewset, base_name="users")
router.register(r'register', UserRegisterViewset, base_name="register")

urlpatterns = [
    # admin
    path('admin/', admin.site.urls),
    # api url
    re_path('api/v1/', include(router.urls)),
    # api login
    re_path('api-auth/', include('rest_framework.urls',
            namespace='rest_framework')),
    path('api/v1/login/', obtain_jwt_token),
]
