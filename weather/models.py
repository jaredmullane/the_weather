from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25) #show name of city as a string with max 25 characters

    def __str__(self): #show city instead of object
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
