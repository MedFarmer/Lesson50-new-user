from django.db import models
from django.contrib.auth.models import AbstractUser

class Customer(AbstractUser):
    second_name = models.CharField(max_length=150, blank=True, verbose_name='Отчество')
    image = models.ImageField(upload_to='avatar', default='default.jpeg', verbose_name='Фотография')
