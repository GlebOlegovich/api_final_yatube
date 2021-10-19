from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet, FollowViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'groups', GroupViewSet)
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename="comments"
)
router.register(r'follow', FollowViewSet, basename="followers")

urlpatterns = [
    # Djoser создаст набор необходимых эндпоинтов.
    # базовые, для управления пользователями в Django:
    path('v1/', include('djoser.urls')),
    # JWT-эндпоинты, для управления JWT-токенами:
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]
