from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from .views import GroupViewSet, PostViewSet, CommentViewSet


router_v1 = DefaultRouter()

router_v1.register(
    'groups', GroupViewSet, basename='groups'
)
router_v1.register(
    'posts', PostViewSet, basename='posts'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments(/(?P<comment_id>\d+)/)?',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
