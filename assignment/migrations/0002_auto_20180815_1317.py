# Generated by Django 2.0 on 2018-08-15 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_page',
            name='submitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='blogsite',
            name='submitted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
