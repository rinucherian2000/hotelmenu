from django.db import models

# Create your models here.


class Food(models.Model):
    name=models.CharField(max_length=120)

class FoodDetail(models.Model):
    item=models.ForeignKey(Food, on_delete=models.CASCADE)
    dish=models.CharField(max_length=250)
    price = models.PositiveIntegerField()
    date = models.DateField(auto_now_add=True)


