# Generated by Django 3.2 on 2021-04-16 13:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True, verbose_name='Name for info')),
                ('instagram_link', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Instagram Link')),
                ('facebook_link', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Facebook Link')),
                ('telegram_link', models.CharField(blank=True, max_length=100, unique=True, verbose_name='Telegram Link')),
                ('youtube_link', models.CharField(blank=True, max_length=100, unique=True, verbose_name='YouTube Link')),
                ('address', models.CharField(blank=True, max_length=250, unique=True, verbose_name='My address')),
                ('background', models.ImageField(upload_to='background', verbose_name='Background image')),
                ('phone_number', models.CharField(blank=True, max_length=17, unique=True, validators=[django.core.validators.RegexValidator('^[0-9]*$'), django.core.validators.MinLengthValidator(5)])),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Info Site',
                'verbose_name_plural': 'Info Site',
            },
        ),
    ]
