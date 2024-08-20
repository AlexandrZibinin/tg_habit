from django.db import models

from config.settings import AUTH_USER_MODEL

NULLABLE = {"blank": True, "null": True}
# IS_NICE_CHOICES = {"Приятная": True, "Полезная": False}
# IS_PUBLIC_CHOICES = {"Публичная": True, "Не публичная": False}

class Habit(models.Model):
    owner = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Пользователь", **NULLABLE)
    place = models.CharField(max_length=100, verbose_name="Место")
    time_action = models.TimeField(auto_now_add=False, auto_now=False, verbose_name="Время (когда выполнить)")
    action = models.CharField(max_length=100, verbose_name="Действие", **NULLABLE)
    is_nice = models.BooleanField(default=False ,verbose_name="Признак приятной привычки")
    related_habit = models.ForeignKey("self", on_delete=models.SET_NULL, verbose_name="Связанная привычка", **NULLABLE)
    period = models.PositiveSmallIntegerField(default=1, verbose_name="Периодичность", help_text="От 1 до 7 дней")
    reward = models.CharField(max_length=150, verbose_name="Награда", **NULLABLE)
    time_to_complete = models.PositiveSmallIntegerField(verbose_name="Время на выполнение", help_text="В минутах")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")



    def __str__(self):
        return f"Привычка:{self.action} Место:{self.place} Когда:{self.time_action}"

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

