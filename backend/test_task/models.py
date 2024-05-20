from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    logo = models.ImageField(upload_to='site/logo/')

    class Meta:
        verbose_name = 'сайт'
        verbose_name_plural = '1. Сайт'

    def __str__(self):
        return self.name


class Benefits(models.Model):
    top_text = models.CharField(max_length=150, blank=False, null=False)
    integer = models.CharField(max_length=150, blank=False, null=False)
    bot_text = models.CharField(max_length=150, blank=False, null=False)
    slug = models.SlugField(max_length=50, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'преимущества'
        verbose_name_plural = '2. Преимущества'

    def __str__(self):
        return self.slug


class Menu(models.Model):
    text = models.CharField(max_length=150, blank=False, null=False)
    slug = models.SlugField(max_length=50, primary_key=True, unique=True)

    class Meta:
        verbose_name = 'меню'
        verbose_name_plural = '2. Меню'

    def __str__(self):
        return self.slug
