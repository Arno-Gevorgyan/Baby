# Generated by Django 3.2 on 2021-04-30 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('children', '0004_person_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='city',
            field=models.CharField(default='Armenia', max_length=40, verbose_name='City'),
        ),
    ]