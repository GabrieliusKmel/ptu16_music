# Generated by Django 4.2.6 on 2023-10-24 11:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music_app', '0002_alter_band_options_remove_band_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='album')),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.band', verbose_name='band')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='content')),
                ('score', models.CharField(max_length=5, verbose_name='score')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.album', verbose_name='album')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='song')),
                ('duration', models.DurationField(verbose_name='duration')),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.album', verbose_name='album')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReviewLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('albumreview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.albumreview', verbose_name='albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
        migrations.CreateModel(
            name='AlbumReviewComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500, verbose_name='content')),
                ('albumreview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music_app.albumreview', verbose_name='albumreview')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
