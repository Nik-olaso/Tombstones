# Generated by Django 5.0.1 on 2024-02-12 16:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="user_id",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="property.users",
            ),
        ),
        migrations.AlterField(
            model_name="users",
            name="user_id",
            field=models.IntegerField(
                blank=True, null=True, verbose_name="ID пользователя"
            ),
        ),
    ]