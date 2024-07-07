from django.db import models
from django.contrib.auth.models import User


class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Countries'


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.RESTRICT)
    timezone = models.CharField(max_length=5)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'


class Group(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    description = models.TextField()
    blocked = models.BooleanField(default=False)
    city = models.ForeignKey(City, on_delete=models.RESTRICT)
    user = models.ForeignKey(User, on_delete=models.RESTRICT)

    def __str__(self) -> str:
        return self.name