from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pregnancy_start_date = models.DateField(null=True, blank=True)
    child_birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username;

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    potential_risk = models.JSONField()
    attract_reason = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    kcal = models.FloatField()

    def __str__(self):
        return self.name

class UserHealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_date = models.DateField(auto_now_add=True)
    diet_record = models.ManyToManyField(Food)
    exercise_record = models.TextField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.record_date}'
