# Generated by Django 4.2.6 on 2023-10-25 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0005_delete_albumreviewcomment'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='posts/img', verbose_name='image'),
        ),
    ]
