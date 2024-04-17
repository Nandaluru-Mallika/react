# Generated by Django 5.0 on 2024-03-13 06:18

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('info', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(5)])),
                ('user_address', models.TextField(max_length=200)),
                ('user_mobile', models.CharField(max_length=15)),
                ('user_email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_name', models.CharField(max_length=100)),
                ('match_date', models.DateField()),
                ('match_time', models.TimeField()),
                ('available_seats_A', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('available_seats_B', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('available_seats_C', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('available_seats_D', models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('match_venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.stadium')),
            ],
            options={
                'verbose_name_plural': 'Matches',
            },
        ),
    ]
