from django.db import models

# Create your models here.

class Phone(models.Model):
    model_name = models.CharField(max_length=50)
    producer =  models.CharField(max_length=30)
    cost = models.IntegerField(default=0)
    operation_system = models.CharField(max_length=70)
    ram = models.IntegerField(default=0)
    core = models.IntegerField(default=0)
    memory = models.IntegerField(default=0)
    display_definition = models.CharField(max_length=20)
    double_camera = models.BooleanField()
    battery = models.IntegerField(default=0)
