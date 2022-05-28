from django.urls import path
from .views import PostCreateAPIView, PostRetrieveAPIView


urlpatterns = [
    path('post/all/', PostCreateAPIView.as_view()),
    path('post/<pk>/', PostRetrieveAPIView.as_view())
]
