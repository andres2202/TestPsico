from django.db import models

class City(models.Model):
    """
    This model represents a city in the country. with an id that automatically increments
    """
    id_city = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
