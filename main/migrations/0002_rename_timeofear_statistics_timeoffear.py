# Generated by Django 4.2.9 on 2024-02-20 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="statistics",
            old_name="timeofear",
            new_name="timeoffear",
        ),
    ]
