# Generated by Django 4.1.7 on 2023-07-22 04:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('creator', '0005_testcreatorcontent_creator_request'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='TestCreatorContent',
            new_name='CreatorContent',
        ),
        migrations.RenameModel(
            old_name='TestCreatorRequest',
            new_name='CreatorRequest',
        ),
        migrations.RenameModel(
            old_name='TestQuestionLabal',
            new_name='QuestionLabal',
        ),
        migrations.RenameModel(
            old_name='TestQuestionLabelGroup',
            new_name='QuestionLabelGroup',
        ),
    ]
