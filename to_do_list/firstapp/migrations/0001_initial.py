# Generated by Django 4.2.4 on 2023-08-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=80)),
                ('is_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
