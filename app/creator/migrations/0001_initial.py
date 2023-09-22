# Generated by Django 4.1.7 on 2023-07-12 18:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desired',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('short_name', models.CharField(max_length=50)),
                ('language', models.CharField(choices=[('en', 'English'), ('fr', 'French'), ('es', 'Spanish')], default='en', max_length=2)),
                ('number_of_students', models.IntegerField()),
                ('age', models.IntegerField()),
                ('grade', models.TextField()),
                ('course', models.TextField()),
                ('description', models.TextField()),
                ('teaching_intention', models.TextField()),
                ('learning_objectives', models.TextField()),
                ('duration', models.TextField()),
                ('educational_approach', models.TextField()),
                ('learning_approach_and_strategies', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('desired', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='creator.desired')),
            ],
        ),
    ]
