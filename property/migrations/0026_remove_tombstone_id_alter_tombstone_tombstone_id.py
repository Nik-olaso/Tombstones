# Generated by Django 5.0.1 on 2024-03-07 13:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("property", "0025_alter_tombstone_link"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="tombstone",
            name="id",
        ),
        migrations.AlterField(
            model_name="tombstone",
            name="tombstone_id",
            field=models.AutoField(
                auto_created=True,
                primary_key=True,
                serialize=False,
                verbose_name="id надгробия",
            ),
        ),
    ]
