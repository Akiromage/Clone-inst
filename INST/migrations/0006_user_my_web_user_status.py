# Generated by Django 4.2.6 on 2023-12-16 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INST', '0005_remove_like_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='my_web',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.TextField(blank=True, null=True),
        ),
    ]