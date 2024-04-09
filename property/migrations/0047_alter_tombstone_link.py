# Generated by Django 5.0.1 on 2024-03-16 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0046_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="link",
            field=models.CharField(
                blank=True,
                default=None,
                max_length=200,
                null=True,
                verbose_name="Ссылка на компанию",
            ),
        ),
    ]