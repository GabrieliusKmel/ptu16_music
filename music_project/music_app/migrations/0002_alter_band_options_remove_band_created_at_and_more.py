# Generated by Django 4.2.6 on 2023-10-24 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='band',
            options={},
        ),
        migrations.RemoveField(
            model_name='band',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='band',
            name='user',
        ),
    ]
