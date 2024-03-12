from django.urls import path, include
from rest_framework import routers

from .views import WeightEntryListView, FitnessGoalListView


weight_entries_router = routers.DefaultRouter()
weight_entries_router.register('', WeightEntryListView, basename='weight-entries')

fitness_goals_router = routers.DefaultRouter()
fitness_goals_router.register('', FitnessGoalListView, basename='fitness-goals')


urlpatterns = [
    path('weight-entries/', include(weight_entries_router.urls)),
    path('fitness-goals/', include(fitness_goals_router.urls)),
]
