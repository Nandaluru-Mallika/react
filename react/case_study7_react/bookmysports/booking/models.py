from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator, RegexValidator
from info.models import Stadium


# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=10, validators=[MinLengthValidator(5)])
    user_address = models.TextField(max_length=200)
    user_mobile = models.CharField(max_length=10, validators=[RegexValidator(r'^[0-9]{10}$', 'Phone number must be 10 digits')])
    user_email = models.EmailField()

    
class Match(models.Model):
    match_name = models.CharField(max_length=100)
    match_venue = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    match_date = models.DateField()
    match_time = models.TimeField()
    available_seats_A = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    available_seats_B = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    available_seats_C = models.IntegerField(validators=[MinValueValidator(0)], blank=True)
    available_seats_D = models.IntegerField(validators=[MinValueValidator(0)], blank=True)

    class Meta:
        verbose_name_plural = "Matches"

    def __str__(self):
        return f"Match at {self.match_venue.stadium_name} on {self.match_date} at {self.match_time}"

    def save(self, *args, **kwargs):
        if not self.pk:  # If creating a new match instance
            self.available_seats_A = self.match_venue.available_seats_A
            self.available_seats_B = self.match_venue.available_seats_B
            self.available_seats_C = self.match_venue.available_seats_C
            self.available_seats_D = self.match_venue.available_seats_D
        super().save(*args, **kwargs)

class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    total_cost = models.IntegerField()
    seats_in_stand_A = models.IntegerField(default=0)
    seats_in_stand_B = models.IntegerField(default=0)
    seats_in_stand_C = models.IntegerField(default=0)
    seats_in_stand_D = models.IntegerField(default=0)
