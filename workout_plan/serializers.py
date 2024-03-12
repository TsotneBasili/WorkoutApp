from rest_framework import serializers
from .models import WorkoutPlan, Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'description', 'instructions', 'target_muscles']


class WorkoutPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkoutPlan
        fields = ['id', 'name', 'workout_frequency', 'goals', 'exercise_types', 'repetitions', 'sets', 'session_duration', 'distance']

