# Generated by Django 5.1 on 2024-08-10 15:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mommymomeatsapp', '0002_ingredient_food_userhealthrecord'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='attraction_reason',
            new_name='attract_reason',
        ),
    ]
