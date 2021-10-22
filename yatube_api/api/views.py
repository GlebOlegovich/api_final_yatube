from rest_framework import filters, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly, ReadOnly
from posts.models import Group, Post

from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer)
from .viewsets import CreateDeleteReadViewSet

# from .mixins import AddToDefaultPermissonsMixin


# Тут добавляем наш миксин на пермишены слева, потому что идет справа налево
# _________________________________________________________________________
# Прошу разрешить оставить эти закоменченные строке, намучался с этим...
# Вдруг мы захоти сделать, что ыб посты видели толь авторизованные юзеры -
# Тогда просто разкоментим и вуаля)
# _________________________________________________________________________
class PostViewSet(
    # AddToDefaultPermissonsMixin,
    viewsets.ModelViewSet
):
    queryset = Post.objects.all()
    # need_to_add_perm = (IsAuthorOrReadOnly,)
    permission_classes = (IsAuthorOrReadOnly,)
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly,)


class FollowViewSet(CreateDeleteReadViewSet):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        return user.follower.all()


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthorOrReadOnly,)

    def _get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self._get_post())

    def get_queryset(self):
        post = self._get_post()
        commments = post.comments.all()
        return commments
