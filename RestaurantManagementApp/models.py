from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cuisine(models.Model):
    cname = models.CharField(max_length=100)

    def __str__(self):
        return self.cname

class Food(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    item_name = models.CharField(max_length=200)
    cuisine = models.ForeignKey(Cuisine,on_delete=models.CASCADE)
    menu_type = models.CharField(max_length=20, choices=[('breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')])
    timings = models.CharField(max_length=100)
    food_type = models.CharField(max_length=20, choices=[('veg', 'Vegetarian'), ('nonveg', 'Non-Vegetarian'), ('both', 'Both')])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__(self):
        return f'{self.item_name},{self.cuisine}'