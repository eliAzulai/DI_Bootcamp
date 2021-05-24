from django.db import models

class Family(models.Model):
    name = models.CharField(max_length=40)
# Create your models here.


class Animal(models.Model):
    name = models.CharField(max_length=40)
    legs = models.IntegerField()      # an integer, the number of legs the animal has
    weight = models.FloatField()  # the average weight of an adult animal of this type
    height = models.FloatField()  # the average height of an adult animal of this type
    speed = models.IntegerField()   # the maximum speed at which this animal can move
    family =  models.ForeignKey(Family, on_delete=models.CASCADE) # the family to which this animal belongs. (Must reference the Family model - see below).
    
    
    