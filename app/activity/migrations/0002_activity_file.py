# Generated by Django 4.1.7 on 2023-05-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='activities/'),
        ),
    ]