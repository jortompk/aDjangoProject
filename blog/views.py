# Create your views here.
from django.shortcuts import render
from blog.models import Post, Tag, Image
from django.http import HttpResponse
#from blog.models import Post

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
# Create your views here.


def tagPage(request, slug):
    tag = Tag.objects.get(slug=slug)
    images = Image.objects.filter(tag=tag).order_by('-date_created')[:6]
    for x in images:
        x.shortDescription = x.description[:130]
        
    context = {}
    context['images'] = images
    context['tag'] = tag

    return render(request, 'main/tag.html', context)


def imageDetailPage(request, slug1, slug2):

    tag = Tag.objects.get(slug=slug1)
    image = Image.objects.get(slug=slug2)

    context = {}
    context['tag'] = tag
    context['image'] = image

    return render(request, 'main/image.html', context)