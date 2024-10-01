from django.db import models

from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        
    name = models.CharField(max_length=250, verbose_name='название', unique=True)
    
    def __str__(self):
        return f'{self.name}'


class News(models.Model):
    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    title = models.CharField(max_length=255, verbose_name='заголовок')
    description = models.CharField(max_length=500, verbose_name='краткое описание')
    content = models.TextField(verbose_name='контент')
    category = models.ForeignKey(
        Category, verbose_name='категория', on_delete=models.CASCADE, related_name='news')
    date = models.DateTimeField(auto_now_add=True, verbose_name='дата добавление')
    auth = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарий'

    name = models.CharField(max_length=100, verbose_name='Имя и фамилия')
    text = models.TextField(verbose_name='текст')
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             verbose_name='новость', related_name='comments')
    date = models.DateField(verbose_name='дата добавление', auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.news.title}'

