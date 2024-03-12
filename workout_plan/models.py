from django.db import models
from django.contrib.auth.models import User


class Exercise(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    instructions = models.TextField()
    target_muscles = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    workout_frequency = models.PositiveIntegerField()  # Times per week
    goals = models.TextField()
    exercise_types = models.ManyToManyField(Exercise, related_name='workout_plans')
    repetitions = models.PositiveIntegerField()
    sets = models.PositiveIntegerField()
    session_duration = models.PositiveIntegerField()  # Duration in minutes
    distance = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.user.name}'s Workout Plan - {self.name} (Exercises: {self.exercise_types})"

