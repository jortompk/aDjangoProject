from django.shortcuts import render
from gallery.models import Tag, Image
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