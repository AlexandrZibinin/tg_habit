from rest_framework.serializers import ModelSerializer

from habits.models import Habit
from habits.validators import LinkedAndRewardValidator, NiceHabitValidator, TimeToCompleteValidator, \
    NiceHabitNotRewardValidator, PeriodCompleteValidator


class HabitSerializer(ModelSerializer):


    class Meta:
        model = Habit
        fields = "__all__"
        validators = [LinkedAndRewardValidator(), NiceHabitValidator(), TimeToCompleteValidator(),
                      NiceHabitNotRewardValidator(), PeriodCompleteValidator()]


