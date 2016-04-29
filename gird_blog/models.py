from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class SiteInfo(models.Model):
    lable = models.CharField(max_length=100)
    title_text = RichTextField()

    def __str__(self):
        return self.lable

class Event(models.Model):
    time = models.DateTimeField()
    summary = RichTextField()

class Newslenta(models.Model):
    time = models.DateTimeField()
    place = models.CharField(max_length=200, blank=True)
    slug = models.SlugField()
    title = models.CharField(max_length=200)
    abstract = RichTextField()
    source = models.CharField(max_length=500)

    class Meta:
        ordering = ['-time']


class Article(models.Model):
    time = models.DateTimeField()
    title = models.CharField(max_length=200)
    abstract = RichTextField()
    content = RichTextField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time']

class Keywords(models.Model):
    tag_word = models.CharField(max_length=30)
    article = models.ManyToManyField(Article)

    def __str__(self):
        return self.tag_word