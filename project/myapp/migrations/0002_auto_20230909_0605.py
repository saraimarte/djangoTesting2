# Generated by Django 3.0.14 on 2023-09-09 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='files',
            name='title',
        ),
        migrations.AddField(
            model_name='files',
            name='file',
            field=models.FileField(blank=True, upload_to='uploads/'),
        ),
    ]
