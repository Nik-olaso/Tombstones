# Generated by Django 5.0.1 on 2024-02-17 13:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0002_alter_tombstone_user_id_alter_users_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tombstone",
            name="birth_year",
        ),
        migrations.RemoveField(
            model_name="tombstone",
            name="death_year",
        ),
    ]
