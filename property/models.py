from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone 


class UsersManager(BaseUserManager):
    def create_user(self, username, email, **extra_fields):
        # Реализовать логику создания пользователя с учетом ваших требований
        user = self.model(username=username, email=email, **extra_fields)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, **extra_fields):
        # Реализовать логику создания суперпользователя
        user = self.create_user(username, email, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def get_profile_image_filepath(self, filename):
    return f'profile_images/{self.pk}/{"profile_image.png"}'


class User(models.Model):
    user = models.CharField(
        max_length=150,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    url = models.CharField(
        max_length=400,
        verbose_name="URL аватарки",
        default=None,
        blank=True,
        null=True,
    )
    created_at = models.DateField(
        auto_now_add=True,
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="ID пользователя",
        blank=True,
        null=True,
    )
    first_name = models.CharField(
        verbose_name="Имя пользователя", max_length=200, blank=True, null=True
    )
    last_name = models.CharField(
        verbose_name="Фамилия пользователя", max_length=200, blank=True, null=True
    )
    on_admin = models.BooleanField(
        verbose_name="Является ли админом", blank=True, null=True
    )
    email = models.EmailField(
        verbose_name="Email", unique=True, blank=True, null=True
    )  # Добавить эту строку

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    objects = UsersManager()


class Tombstone(models.Model):
    tombstone_id = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name="id надгробия",
    )
    create_date = models.DateTimeField(
        verbose_name="Время создания",
        blank=True,
        null=True,
    )
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    user_role = models.CharField(
        max_length=200,
        verbose_name="Роль пользователя",
        blank=True,
        null=True,
    )
    company_name = models.CharField(
        max_length=18,
        verbose_name="Название компании",
        default=None,
    )
    logo = models.ImageField(
        upload_to="uploads_model",
        default=None,
        verbose_name="Логотип",
    )
    birth_year = models.IntegerField(
        verbose_name="Год создания",
        validators=[MaxValueValidator(2024, message="Максимум можно указать 2024 год")],
        default=None,
    )
    death_year = models.IntegerField(
        verbose_name="Год смерти",
        validators=[MaxValueValidator(2024, message="Максимум можно указать 2024 год")],
        default=None,
    )
    alternate_name = models.CharField(
        max_length=200,
        verbose_name="Альтернативное название",
        blank=True,
        null=True,
    )
    people = models.CharField(
        max_length=200,
        verbose_name="Ключевые люди и их роли",
        blank=True,
        null=True,
    )
    link = models.CharField(
        max_length=200,
        verbose_name="Ссылка на компанию",
        default=None,
        blank=True,
        null=True,
    )
    characteristic = models.TextField(
        verbose_name="Характеристики компании",
        blank=True,
        null=True,
    )
    description = models.TextField(
        verbose_name="Описание компании",
        blank=True,
        null=True,
    )
    death_cause = models.TextField(
        verbose_name="Причина смерти компании",
        blank=True,
        null=True,
    )
    count_employee = models.IntegerField(
        verbose_name="Количество сотрудников",
        default=None,
        blank=True,
        null=True,
    )
    revenue = models.IntegerField(
        verbose_name="Доход компании",
        default=None,
        blank=True,
        null=True,
    )
    score_company = models.IntegerField(
        verbose_name="Оценочная стоимость на рынке",
        default=None,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.company_name}\n{self.birth_year}-{self.death_year}"

    objects = models.Manager()


class Comment(models.Model):
    comment = models.TextField(max_length=500, verbose_name="Комментарий",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время отправки",)
    user = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name="ID пользователя",)
    tombstone = models.ForeignKey(Tombstone, on_delete=models.PROTECT, verbose_name="ID надгробия",)
