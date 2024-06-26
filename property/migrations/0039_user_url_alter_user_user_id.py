# Generated by Django 5.0.1 on 2024-03-11 21:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0038_delete_userprofile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="url",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=400,
                null=True,
                verbose_name="URL аватарки",
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="ID пользователя",
            ),
        ),
    ]
