from rest_framework import serializers
from .models import WeightEntry, FitnessGoal


class WeightEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightEntry
        fields = ['id', 'date', 'weight']


class FitnessGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessGoal
        fields = ['id', 'weight_goal', 'exercise_achievement']
