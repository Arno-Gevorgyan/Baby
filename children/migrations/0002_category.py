# Generated by Django 3.2 on 2021-04-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='Name Category')),
                ('about', models.TextField(verbose_name='About Category')),
                ('photo', models.ImageField(upload_to='Category', verbose_name='Photo')),
                ('url', models.SlugField(unique=True, verbose_name='Url')),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10, verbose_name='Status')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
