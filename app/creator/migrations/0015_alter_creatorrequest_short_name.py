# Generated by Django 4.2.2 on 2023-09-22 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0014_consolidatedquestions_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creatorrequest',
            name='short_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]