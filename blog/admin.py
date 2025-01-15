# Register your models here.

from django.contrib import admin
from blog.models import Tag, Post, Image

class ImageAdmin(admin.ModelAdmin):
    pass

class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)
