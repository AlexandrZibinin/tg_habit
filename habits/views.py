
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView

from habits.models import Habit
from habits.pagination import CustomHabitPagination
from habits.serializer import HabitSerializer
from users.permissions import IsOwnerReadOnly, PublicReadOnly


class HabitListAPIView(ListAPIView):
    serializer_class = HabitSerializer
    pagination_class = CustomHabitPagination
    permission_classes = (IsOwnerReadOnly | PublicReadOnly, )


    def get(self, request):
        queryset = Habit.objects.all()
        paginated_queryset = self.paginate_queryset(queryset)
        serializer = HabitSerializer(paginated_queryset, many=True)
        return self.get_paginated_response(serializer.data)

class HabitCreateAPIView(CreateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()

    def perform_create(self, serializer):
        habit = serializer.save()
        habit.owner = self.request.user
        habit.save()


class HabitRetrieveAPIView(RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerReadOnly,)



class HabitDestroyAPIView(DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerReadOnly,)


class HabitUpdateAPIView(UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = (IsOwnerReadOnly,)



