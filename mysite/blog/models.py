from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    # наименование
    title = models.CharField(max_length=250)
    #  техническая информация - ссылка на публикацию
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    # автор - первичный ключ
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    # текст поста
    body = models.TextField()
    # дата публикации
    publish = models.DateTimeField(default=timezone.now)
    # дата создания
    created = models.DateTimeField(auto_now_add=True)
    # дата редактирования
    updated = models.DateTimeField(auto_now=True)
    # статус публикации
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    class Meta:
        ordering = ('-publish',)
    def __str__(self):
        return self.title

class Author(models.Model):
    id_author = models.IntegerField(primary_key=True)
    name_first = models.CharField(max_length=250)
    name_second = models.CharField(max_length=250)
    telefon = models.IntegerField(max_length=10) #без учета префикса +
    email = models.CharField(max_length=250)
    registration = models.DateTimeField(default=timezone.now)
    rating = models.IntegerField(max_length=2)
    def __str__(self):
        return self.title

class Theme(models.Model):
    body = models.TextField()
    def __str__(self):
        return self.title

