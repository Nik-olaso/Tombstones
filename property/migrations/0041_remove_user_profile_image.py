# Generated by Django 5.0.1 on 2024-03-14 18:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0040_remove_user_username_user_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="profile_image",
        ),
    ]
