from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Rabota(models.Model):
    title = models.CharField(max_length=249, blank=True, verbose_name='Название проекта')
    users = models.ManyToManyField(User, blank=True, verbose_name='Участники проекта')
    project_type = models.ManyToManyField('ProjectType', blank=True, verbose_name='Вид')
    info = models.CharField(max_length=249, blank=True, verbose_name='Задача')
    info_plan = models.CharField(max_length=249, blank=True, verbose_name='Цель')
    info_finish = models.CharField(max_length=249, blank=True, verbose_name='Решение')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, verbose_name='Заказчик')
    step1 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 1')
    photo_step1 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 1')
    step2 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 2')
    photo_step2 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 2')
    step3 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 3')
    photo_step3 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 3')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

class Customer(models.Model):
    title = models.CharField(max_length=249, blank=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'

class ProjectType(models.Model):
    title = models.CharField(max_length=249, verbose_name='Название')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'