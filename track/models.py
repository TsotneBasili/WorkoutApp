from django.db import models
from django.contrib.auth.models import User


class WeightEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.user.name} - {self.date}: {self.weight} kg"


class FitnessGoal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight_goal = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    exercise_achievement = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.user.name}'s Fitness Goal"
