# Create your views here.
from django.shortcuts import render
from blog.models import Post
from django.http import HttpResponse


from blog.models import Post

def blog_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context = {
        "posts": posts,
    }
    return render(request, "blog/index.html", context)

def blog_tag(request, tag):
    posts = Post.objects.filter(
        tag__name__contains=tag
    ).order_by("-created_on")
    context = {
        "tags": tag,
        "posts": posts,
    }

    return render(request, "blog/tag.html", context)