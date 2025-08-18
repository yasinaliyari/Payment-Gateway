from django.shortcuts import render
from django.views.generic import ListView
from blog.models import Post


class BlogPostListView(ListView):
    model = Post
    context_object_name = "posts"
