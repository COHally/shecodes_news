# Generated by Django 4.2.7 on 2023-12-05 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_remove_customuser_bio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.URLField(blank=True),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]