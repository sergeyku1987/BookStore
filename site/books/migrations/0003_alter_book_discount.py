# Generated by Django 4.2.7 on 2024-05-02 12:51

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20240501_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='discount',
            field=models.PositiveIntegerField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(99)]),
        ),
    ]
