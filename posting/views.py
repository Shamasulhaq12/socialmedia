from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post


class PostCreateAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostRetrieveAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
