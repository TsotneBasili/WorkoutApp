# Generated by Django 4.2.4 on 2024-03-10 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout_plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutplan',
            name='exercise_types',
            field=models.ManyToManyField(blank=True, null=True, related_name='workout_plans', to='workout_plan.exercise'),
        ),
    ]