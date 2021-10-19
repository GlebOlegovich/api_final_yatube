from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import LimitOffsetPagination
from api.permissions import IsOwnerOrReadOnly, ReadOnly
from posts.models import Group, Post, Follow
from posts.models import User
from rest_framework import filters

from .permissions import set_permissions
from .serializers import CommentSerializer, GroupSerializer, PostSerializer, FollowSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination
    # def get_permissions(self):
    #     return(set_permissions(self))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (ReadOnly,)

class FollowViewSet(viewsets.ModelViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    # permission_classes = (IsOwnerOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        #print(self.request.user)

    def get_queryset(self):
        # follow = Follow.objects.filter(user=)
        user = get_object_or_404(User, username = self.request.user)
        return user.follower.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # need_to_add_perm = (IsOwnerOrReadOnly,)
    permission_classes = (IsOwnerOrReadOnly,)
    # def get_permissions(self):
    #     return(set_permissions(self))

    def _get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self._get_post())

    def get_queryset(self):
        post = self._get_post()
        commments = post.comments.all()
        return commments
