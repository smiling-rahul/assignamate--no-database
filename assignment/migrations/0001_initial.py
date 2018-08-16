# Generated by Django 2.0 on 2018-08-16 06:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='assignment', max_length=30)),
                ('discription', models.CharField(max_length=500)),
                ('created', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Assignment_answered_by',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_assignment', models.CharField(max_length=30)),
                ('name_of_teacher', models.CharField(blank=True, max_length=150)),
                ('assigner_username', models.CharField(blank=True, max_length=150)),
                ('assignment_id', models.IntegerField()),
                ('answer_string', models.CharField(max_length=400)),
                ('marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Assignmentlikecounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_like', models.IntegerField(default=0)),
                ('assignment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Blog_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('text', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='blog_image/')),
                ('submitted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Blogsite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quotes', models.CharField(blank=True, max_length=100)),
                ('discription', models.CharField(blank=True, max_length=500)),
                ('background_image', models.ImageField(upload_to='blogger_image/')),
                ('submitted', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='question_image//%Y/%m/%d/')),
                ('answer', models.CharField(max_length=500)),
                ('option_a', models.CharField(default=0, max_length=200)),
                ('option_b', models.CharField(default=0, max_length=200)),
                ('option_c', models.CharField(default=0, max_length=200)),
                ('option_d', models.CharField(default=0, max_length=200)),
                ('number_of_right_answered', models.IntegerField(default=0)),
                ('number_of_wrong_answered', models.IntegerField(default=0)),
                ('positive_marks', models.IntegerField(default=0)),
                ('negative_marks', models.IntegerField(default=0)),
                ('hint', models.CharField(blank=True, max_length=500)),
                ('tags', models.CharField(blank=True, max_length=45)),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Assignment')),
            ],
        ),
        migrations.CreateModel(
            name='Studymaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=20)),
                ('discription', models.CharField(max_length=500)),
                ('document', models.FileField(upload_to='documents//%Y/%m/%d/')),
                ('uploaded_at', models.DateField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='blog_page',
            name='blog_site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignment.Blogsite'),
        ),
        migrations.AddField(
            model_name='blog_page',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]