# Generated by Django 2.2.6 on 2019-11-29 08:02

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('image', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('-created', 'user')},
        ),
        migrations.AddField(
            model_name='image',
            name='user_liked',
            field=models.ManyToManyField(blank=True, related_name='image_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]