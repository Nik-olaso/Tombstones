# Generated by Django 5.0.1 on 2024-02-29 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0011_alter_tombstone_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tombstone",
            name="logo",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="photos/%Y/%m/%d/",
                verbose_name="Логотип",
            ),
        ),
    ]
