# Generated by Django 5.1.4 on 2025-01-08 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
