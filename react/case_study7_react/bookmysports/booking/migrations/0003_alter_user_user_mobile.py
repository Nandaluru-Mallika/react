# Generated by Django 5.0 on 2024-03-15 08:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_mobile',
            field=models.CharField(max_length=10, validators=[django.core.validators.RegexValidator('^[0-9]{10}$', 'Phone number must be 10 digits')]),
        ),
    ]
