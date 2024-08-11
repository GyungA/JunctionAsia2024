from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pregnancy_start_date = models.DateField(null=True, blank=True)
    child_birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username;

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    verified = models.BooleanField(default=False)
    attract_reason = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    ingredients = models.ManyToManyField(Ingredient)
    kcal = models.IntegerField()

    def __str__(self):
        return self.name

class PotentialRisk(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    pregnancy_week_start = models.IntegerField()
    pregnancy_week_end = models.IntegerField()
    risk_level = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.ingredient.name} ({self.pregnancy_week_start} - {self.pregnancy_week_end} weeks: {self.risk_level}'

class Substitution(models.Model):
    substitutable_attract_reason = models.CharField(max_length=255)
    recommended_food = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.recommended_food} (for {self.substitutable_attract_reason})'

class UserHealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    record_date = models.DateField(auto_now_add=True)
    diet_record = models.ManyToManyField(Food)
    exercise_record = models.TextField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.record_date}'
