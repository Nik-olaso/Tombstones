# Generated by Django 5.0.1 on 2024-03-22 19:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0050_alter_tombstone_link"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="company_name",
            field=models.CharField(
                default=None, max_length=30, verbose_name="Название компании"
            ),
        ),
    ]