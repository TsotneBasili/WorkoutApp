from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from track.models import WeightEntry, FitnessGoal
from track.serializers import WeightEntrySerializer, FitnessGoalSerializer


class WeightEntryListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = WeightEntrySerializer
    queryset = WeightEntry.objects.all()

    def list(self, request, *args, **kwargs):
        pk = self.request.user.pk

        queryset = WeightEntry.objects.filter(user=pk)
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
            weightentry = WeightEntry.objects.get(pk=pk)

            if weightentry.user == request.user:
                serializer = self.get_serializer(weightentry)
                return Response(serializer.data)
            else:
                return Response({"detail": "weight entry does not belong to the currently logged-in user."})

        except:
            return Response({"detail": "weight entry not found."})


class FitnessGoalListView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = FitnessGoalSerializer
    queryset = FitnessGoal.objects.all()

    def list(self, request, *args, **kwargs):
        pk = self.request.user.pk

        queryset = FitnessGoal.objects.filter(user=pk)
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
            fitness_goal = FitnessGoal.objects.get(pk=pk)

            if fitness_goal.user == request.user:
                serializer = self.get_serializer(fitness_goal)
                return Response(serializer.data)
            else:
                return Response({"detail": "fitness goal does not belong to the currently logged-in user."})

        except:
            return Response({"detail": "fitness goal not found."})
