from django.urls import path
from blog.views import BlogPostListView

urlpatterns = [
    path("post/", BlogPostListView.as_view(template_name="blog/index.html")),
]
