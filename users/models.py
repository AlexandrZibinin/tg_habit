from django.db import models

from django.contrib.auth.models import AbstractUser

NULLABLE = {"blank": True, "null": True}

class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="почта")
    phone = models.CharField(max_length=35, **NULLABLE,
                             verbose_name="телефон")
    tg_name = models.CharField(max_length=35, **NULLABLE,
                             verbose_name="телеграм")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
