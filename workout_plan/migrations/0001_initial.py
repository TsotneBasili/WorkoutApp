# Generated by Django 4.2.4 on 2024-03-10 10:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('instructions', models.TextField()),
                ('target_muscles', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('workout_frequency', models.PositiveIntegerField()),
                ('goals', models.TextField()),
                ('repetitions', models.PositiveIntegerField()),
                ('sets', models.PositiveIntegerField()),
                ('session_duration', models.PositiveIntegerField()),
                ('distance', models.PositiveIntegerField()),
                ('exercise_types', models.ManyToManyField(related_name='workout_plans', to='workout_plan.exercise')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
