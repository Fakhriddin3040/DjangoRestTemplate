# Generated by Django 5.0.7 on 2024-11-29 11:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("category", "0004_remove_category_synced_at"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="category",
            name="ext_parent_title",
        ),
    ]
