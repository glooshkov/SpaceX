# Generated by Django 5.0.4 on 2024-05-13 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefits',
            fields=[
                ('top_text', models.CharField(max_length=150)),
                ('integer', models.CharField(max_length=150)),
                ('bot_text', models.CharField(max_length=150)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'преимущества',
                'verbose_name_plural': '2. Преимущества',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('text', models.CharField(max_length=150)),
                ('slug', models.SlugField(primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'verbose_name': 'меню',
                'verbose_name_plural': '2. Меню',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('logo', models.ImageField(upload_to='site/logo/')),
            ],
            options={
                'verbose_name': 'сайт',
                'verbose_name_plural': '1. Сайт',
            },
        ),
    ]
