# Generated by Django 3.2 on 2021-04-30 14:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0003_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation date'),
        ),
    ]
