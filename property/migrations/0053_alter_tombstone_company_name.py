# Generated by Django 5.0.1 on 2024-03-22 19:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0052_alter_tombstone_company_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="company_name",
            field=models.CharField(
                default=None, max_length=18, verbose_name="Название компании"
            ),
        ),
    ]