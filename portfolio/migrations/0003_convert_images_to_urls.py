# Generated by Django 4.2.7 on 2025-07-21 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_alter_blogpost_featured_image_alter_course_thumbnail_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='featured_image',
            field=models.URLField(blank=True, help_text='Link đến ảnh đại diện bài viết', verbose_name='Link ảnh đại diện'),
        ),
        migrations.AlterField(
            model_name='course',
            name='thumbnail',
            field=models.URLField(blank=True, help_text='Link đến ảnh thumbnail khóa học', verbose_name='Link ảnh thumbnail'),
        ),
        migrations.AlterField(
            model_name='podcastepisode',
            name='thumbnail',
            field=models.URLField(blank=True, help_text='Link đến ảnh thumbnail episode', verbose_name='Link ảnh thumbnail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.URLField(blank=True, help_text='Link đến ảnh đại diện (VD: https://images.unsplash.com/...)', verbose_name='Link ảnh đại diện'),
        ),
    ]
