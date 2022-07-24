from django.db import models

class TypeSpecialty(models.Model):  
    id_specialty = models.AutoField(primary_key=True)
    nameSpecialty = models.CharField(max_length=50)
    