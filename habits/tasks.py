from celery import shared_task

from habits.models import Habit
from habits.services import send_tg_message
from users.models import User


@shared_task
def send_message(email, pk):

    user = User.objects.get(email=email)
    habit = Habit.objects.get(pk=pk)

    if user.tg_id_chat:
        message = f"Я буду {habit.action} в {habit.time_to_complete} в {habit.place}"
        send_tg_message(user.tg_id_chat, message)
