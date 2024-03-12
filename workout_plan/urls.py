from django.urls import path, include
from rest_framework import routers

from workout_plan.views import WorkoutPlanView, ExerciseView

workout_plan_router = routers.DefaultRouter()
workout_plan_router.register('', WorkoutPlanView, basename='workout-plan')

exercise_router = routers.DefaultRouter()
exercise_router.register('', ExerciseView, basename='exersice')


urlpatterns = [
    path('plan/', include(workout_plan_router.urls)),
    path('exercise/', include(exercise_router.urls)),
]
