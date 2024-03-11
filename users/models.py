from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')
    chat_id = models.TextField(verbose_name='id чата в телеграмм', **NULLABLE)
    telegram_user_name = models.CharField(max_length=200, verbose_name='имя в телеграмм', unique=True, **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
