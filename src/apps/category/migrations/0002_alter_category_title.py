# Generated by Django 5.1.1 on 2024-11-21 12:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="title",
            field=models.CharField(max_length=120),
        ),
    ]
