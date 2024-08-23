import datetime

from celery import shared_task

from habits.models import Habit
from habits.services import send_tg_message


@shared_task
def send_message():
    habits = Habit.objects.all()
    current_time = datetime.datetime.now().time()

    for habit in habits:
        if habit.time_action == current_time:
            user_id = habit.owner.tg_id_chat
            if user_id:
                message = f"Я буду {habit.action} в {habit.time_to_complete} в {habit.place}"
                send_tg_message(user_id, message)
