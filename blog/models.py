from django.db import models
from django.urls import reverse


# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    class Meta:
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField('Опубликовано', auto_now_add=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    views = models.IntegerField('Количество просмотров', default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='posts')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
