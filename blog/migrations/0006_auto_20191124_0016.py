# Generated by Django 2.2.6 on 2019-11-24 00:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='tag',
            new_name='tags',
        ),
    ]
