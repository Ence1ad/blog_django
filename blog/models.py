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
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class Tag(models.Model):
    title = models.CharField(max_length=55)
    slug = models.SlugField(max_length=55, verbose_name='Url', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['title']


class Post(models.Model):
    title = models.CharField('Заголовок', max_length=255)
    slug = models.SlugField('URL', max_length=255, unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField('Опубликовано', auto_now_add=True)
    photo = models.ImageField(upload_to="photo/%Y/%m/%d/", blank=True)
    views = models.IntegerField('Количество просмотров', default=0)
    category = models.ForeignKey(Category,
                                 on_delete=models.PROTECT,
                                 related_name='posts', verbose_name='Категория')
    tag = models.ManyToManyField(Tag, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-created_at']
