# Generated by Django 5.0.7 on 2024-09-17 05:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authorization", "0002_alter_user_managers_profile_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="birth_date",
            field=models.DateField(blank=True, null=True, verbose_name="Дата рождения"),
        ),
    ]
