# Generated by Django 4.2.7 on 2023-12-05 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_like'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Like',
        ),
    ]
