# Generated by Django 5.0.1 on 2024-03-09 17:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0031_users_email"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
