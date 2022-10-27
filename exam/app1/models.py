from django.db import models
from django.contrib.auth.models import User

class Yozuvchi(models.Model):
    name = models.CharField(max_length=30,null=True)
    age = models.PositiveIntegerField(null=True)
    job = models.CharField(max_length=30,null=True)

    def __str__(self):
        return self.name


class NEWS(models.Model):
    sarlavha = models.CharField(max_length=30,null=True)
    sana = models.DateTimeField(null=True, blank=True, default=None)
    mavzu = models.CharField(max_length=30,null=True)
    math = models.ForeignKey(Yozuvchi,on_delete=models.CASCADE,null=True,default=None)

    def __str__(self):
        return self.sarlavha