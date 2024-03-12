from django.db import migrations
import json

def load_exercises(apps, schema_editor):
    Exercise = apps.get_model('workout_plan', 'Exercise')

    with open('workout_plan/exercises.json', 'r') as file:
        exercises = json.load(file)

    for exercise_data in exercises:
        Exercise.objects.create(**exercise_data['fields'])


class Migration(migrations.Migration):

    dependencies = [
        ('workout_plan', '0003_alter_workoutplan_exercise_types'),
    ]

    operations = [
        migrations.RunPython(load_exercises),
    ]
