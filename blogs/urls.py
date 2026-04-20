from django.urls import path
from .views import (
    BlogListCreateView, BlogRetrieveUpdateDestroyView,
    CommentListCreateView, CommentRetrieveUpdateDestroyView
)

urlpatterns = [
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogRetrieveUpdateDestroyView.as_view(), name='blog-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail'),
]

