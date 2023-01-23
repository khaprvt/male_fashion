from django.urls import path
from .views import BlogListView, BlogDetailView, CommentCreateView

app_name = 'blogs'

urlpatterns = [
    path('', BlogListView.as_view(), name='list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('<int:pk>/comment/', CommentCreateView.as_view(), name='comment')
]