from rest_framework import serializers

from habits.models import Habit


class LinkedAndRewardValidator:
    def __call__(self, value):
        linked = value.get("related_habit")
        reward = value.get("reward")

        if linked and reward:
            raise serializers.ValidationError(
                "Исключено одновременный выбор связанной привычки и указания вознаграждения.")

class TimeToCompleteValidator:
    def __call__(self, value):
        time_to_complete = value.get("time_to_complete") * 60

        if time_to_complete > 120:
            raise serializers.ValidationError("Время выполнения должно быть не больше 120 секунд.")


class NiceHabitValidator:
    def __call__(self, value):
        related_habit = value.get("related_habit")

        if related_habit:
            habit = Habit.objects.get(pk=related_habit.id)
            if not habit.is_nice:
                raise serializers.ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


class NiceHabitNotRewardValidator:
    def __call__(self, value):
        is_nice = value.get("is_nice")
        if is_nice:
            linked = value.get("related_habit")
            reward = value.get("reward")
            if linked or reward:
                raise serializers.ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")


class PeriodCompleteValidator:
    def __call__(self, value):
        period = value.get("period")
        if period < 1:
            raise serializers.ValidationError("Нельзя выполнять привычку реже, чем 1 раз в 7 дней.")