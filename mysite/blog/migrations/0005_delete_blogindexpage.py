# Generated by Django 4.1.5 on 2023-01-23 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_blogindexpage"),
    ]

    operations = [
        migrations.DeleteModel(
            name="BlogIndexPage",
        ),
    ]
