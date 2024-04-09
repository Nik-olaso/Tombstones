# Generated by Django 5.0.1 on 2024-03-06 21:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0018_alter_tombstone_create_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="birth_year",
            field=models.IntegerField(
                default=None, max_length=4, verbose_name="Год создания"
            ),
        ),
        migrations.AlterField(
            model_name="tombstone",
            name="company_name",
            field=models.CharField(
                default=None, max_length=200, verbose_name="Название компании"
            ),
        ),
        migrations.AlterField(
            model_name="tombstone",
            name="death_year",
            field=models.IntegerField(
                default=None, max_length=4, verbose_name="Год смерти"
            ),
        ),
    ]
