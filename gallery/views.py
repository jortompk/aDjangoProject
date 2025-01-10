from django.shortcuts import render

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