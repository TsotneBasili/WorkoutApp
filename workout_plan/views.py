from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from workout_plan.models import WorkoutPlan, Exercise
from workout_plan.serializers import ExerciseSerializer, WorkoutPlanSerializer


class WorkoutPlanView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkoutPlanSerializer
    queryset = WorkoutPlan.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = WorkoutPlan.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.pk
        serializer = self.serializer_class(data=mutable_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            workout_plan = WorkoutPlan.objects.get(pk=pk)

            if workout_plan.user == request.user:
                serializer = self.get_serializer(workout_plan)
                return Response(serializer.data)
            else:
                return Response({"detail": "workout plan does not belong to the currently logged-in user."})

        except WorkoutPlan.DoesNotExist:
            return Response({"detail": "workout plan not found."})

    def update(self, request, pk=None, *args, **kwargs):
        try:
            workout_plan = WorkoutPlan.objects.get(pk=pk)

            if workout_plan.user == request.user:
                serializer = self.get_serializer(workout_plan, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user)
                return Response(serializer.data)

            else:
                return Response({"detail": "You do not have permission to update this workout plan."})

        except WorkoutPlan.DoesNotExist:
            return Response({"detail": "workout plan not found."})

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            workout_plan = WorkoutPlan.objects.get(pk=pk)

            if workout_plan.user == request.user:
                workout_plan.delete()
                return Response({"detail": "Workout plan deleted successfully."})

            else:
                return Response({"detail": "You do not have permission to delete this workout plan."})

        except WorkoutPlan.DoesNotExist:
            return Response({"detail": "workout plan not found."})


class ExerciseView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ExerciseSerializer
    queryset = Exercise.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = Exercise.objects.filter(user=request.user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        mutable_data = request.data.copy()
        mutable_data['user'] = request.user.pk
        serializer = self.serializer_class(data=mutable_data)

        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        try:
            exercise = Exercise.objects.get(pk=pk)

            if exercise.user == request.user:
                serializer = self.get_serializer(exercise)
                return Response(serializer.data)
            else:
                return Response({"detail": "exercise does not belong to the currently logged-in user."})

        except Exercise.DoesNotExist:
            return Response({"detail": "exercise not found."})

    def update(self, request, pk=None, *args, **kwargs):
        try:
            exercise = Exercise.objects.get(pk=pk)

            if exercise.user == request.user:
                serializer = self.get_serializer(exercise, data=request.data, partial=True)
                serializer.is_valid(raise_exception=True)
                serializer.save(user=request.user)
                return Response(serializer.data)

            else:
                return Response({"detail": "You do not have permission to update this exercise."})

        except Exercise.DoesNotExist:
            return Response({"detail": "exercise not found."})

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            exercise = Exercise.objects.get(pk=pk)

            if exercise.user == request.user:
                exercise.delete()
                return Response({"detail": "Exercise deleted successfully."})

            else:
                return Response({"detail": "You do not have permission to delete this exercise."})

        except Exercise.DoesNotExist:
            return Response({"detail": "exercise not found."})
