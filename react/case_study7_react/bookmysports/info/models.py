from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator


# Create your models here.

class Stadium(models.Model):
    stadium_name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    available_seats_A = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    available_seats_B = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    available_seats_C = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    available_seats_D = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    stadium_address = models.TextField()

    def __str__(self):
        return self.stadium_name
    
class Team(models.Model):
    team_name = models.CharField(max_length=100)
    abbrevation = models.CharField(max_length=6, null=True)
    team_members = models.TextField()
    home_ground = models.OneToOneField(Stadium, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


