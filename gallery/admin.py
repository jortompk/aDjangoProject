from django.contrib import admin
from gallery.models import Tag, Image

class TagAdmin(admin.ModelAdmin):
    pass

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)

# Register your models here.
