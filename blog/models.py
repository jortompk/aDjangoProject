# blog/models.py
# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
from django.template.defaultfilters import slugify
from django_resized import ResizedImageField
from django.utils import timezone
from uuid import uuid4
from django.urls import reverse



class Tag(models.Model):
    title = models.CharField(null=True, blank=True, max_length=200)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('category-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.title, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Tag, self).save(*args, **kwargs)

class Image(models.Model):
    description = models.TextField(null=True, blank=True)
    altText = models.TextField(null=True, blank=True)
    tags = models.CharField(null=True, blank=True, max_length=300)

    squareImage = ResizedImageField(size=[1000, 1000], crop=['middle', 'center'], default='default_square.jpg', upload_to='square')
    landImage = ResizedImageField(size=[2878, 1618], crop=['middle', 'center'], default='default_land.jpg', upload_to='landscape')
    tallImage = ResizedImageField(size=[1618, 2878], crop=['middle', 'center'], default='default_tall.jpg', upload_to='tall')

    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)

    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {}'.format(self.category.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.tag.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.tag.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    tags = models.CharField(null=True, blank=True, max_length=300)
    tag = models.ForeignKey(Tag, null=True, blank=True, on_delete=models.CASCADE)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    slug = models.SlugField(max_length=500, unique=True, blank=True, null=True)
    #    tags = models.ManyToManyField("Tag", related_name="posts")
    '''
    def __str__(self):
        return self.title
    
        description = models.TextField(null=True, blank=True)'''


    def __str__(self):
        return '{} {}'.format(self.category.title, self.uniqueId)

    def get_absolute_url(self):
        return reverse('image-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())
        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.tag.title, self.uniqueId))


        self.slug = slugify('{} {}'.format(self.tag.title, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())
        super(Image, self).save(*args, **kwargs)
