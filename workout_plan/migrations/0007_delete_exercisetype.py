# Generated by Django 4.2.4 on 2024-03-12 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workout_plan', '0006_exercisetype'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ExerciseType',
        ),
    ]
