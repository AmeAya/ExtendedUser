from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
# AbstractUser - Модель встроенного user с уже созданными полями и менеджерами и т.д.
# Используем его, когда не нужно с нуля писать новую модель для пользователей,
# а нужно, просто дополнить(добавить новые поля)


class ExtendedUser(AbstractUser):
    tax_code = models.CharField(max_length=12)
    phone = models.CharField(max_length=20)
    social_page = models.CharField(max_length=255)
