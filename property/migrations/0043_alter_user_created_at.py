# Generated by Django 5.0.1 on 2024-03-14 18:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0042_user_created_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="created_at",
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]