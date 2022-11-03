from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

## СТРАНИЦА РАБОТЫ
class Rabota(models.Model):
    title = models.CharField(max_length=249, blank=True, verbose_name='Название проекта')
    users = models.ManyToManyField(User, blank=True, verbose_name='Участники проекта')
    project_type = models.ManyToManyField('ProjectType', blank=True, verbose_name='Вид', related_name='rabota_type')
    info = models.CharField(max_length=249, blank=True, verbose_name='Задача')
    project_info = models.CharField(max_length=249, blank=True, verbose_name='Инфо')
    info_plan = models.CharField(max_length=249, blank=True, verbose_name='Цель')
    info_finish = models.CharField(max_length=249, blank=True, verbose_name='Решение')
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, blank=True, verbose_name='Заказчик')
    photo = models.ImageField(upload_to='rabota/%Y/%m/%d', blank=True, verbose_name='Фото')
    step1 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 1', null=True)
    photo_step1 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 1')
    step2 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 2')
    photo_step2 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 2')
    step3 = models.CharField(max_length=249, blank=True, verbose_name='Шаг 3')
    photo_step3 = models.ImageField(upload_to='rabota/%Y/%m/%d/', blank=True, verbose_name='Фото шага 3')
    slug = models.SlugField(blank=True, unique=True, db_index=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def get_absolute_url(self):
        return reverse('rabota', kwargs={'slug': self.slug})

    def count(self):
        return Rabota.objects.all().count()
        

## КЛАСС ЗАКАЗЧИКА
class Customer(models.Model):
    title = models.CharField(max_length=249, blank=True)

    def __str__(self):
        return self.title

    class Meta():
        verbose_name = 'Заказчик'
        verbose_name_plural = 'Заказчики'


## КЛАСС ТИП РАБОТЫ
class ProjectType(models.Model):
    title = models.CharField(max_length=249, verbose_name='Название')
    slug = models.SlugField(blank=True, unique=True, db_index=True, verbose_name='Имя', null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

    def get_absolute_url(self):
        return reverse('kategorii', kwargs={'project_type_slug': self.slug})

    def count(self):
        return Rabota.objects.all().count()


## КЛАСС ПРОФИЛЬ ПОЛЬЗОВАТЕЛЯ
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, editable=False)
    photo = models.ImageField(upload_to='user/avatar/%Y/%m/%d/', blank=True, verbose_name="Аватарка")
    doljnost = models.CharField(max_length=49, blank=True, verbose_name='Должность')
    hobi = models.TextField(blank=True, verbose_name='Увлечения')

    def __str__(self):
        return f'Логин: {self.user.username} | {self.user.first_name}  {self.user.last_name} — ++ для красоты'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'


## АВТОМАТИЧЕСКОЕ ПРИСВОЕНИЕ ПРОФИЛЯ НОВОМУ ПОЛЬЗОВАТЕЛЮ  
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()