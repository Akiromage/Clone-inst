# Generated by Django 4.2.6 on 2024-02-01 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('INST', '0007_saveposts'),
    ]

    operations = [
        migrations.RenameField(
            model_name='saveposts',
            old_name='save',
            new_name='saves_posts',
        ),
    ]
