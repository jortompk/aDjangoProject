# blog/models.py
# Create your models here.
from django.db import models


class Tag(models.Model):
    tag_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "tags"

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name="posts")

    def __str__(self):
        return self.title