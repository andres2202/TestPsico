from django.contrib import admin
from .models.city import City
from .models.typeSpecialty import TypeSpecialty
from .models.psychologist import Psychologist

# Register your models here.

admin.site.register(City)
admin.site.register(TypeSpecialty)
admin.site.register(Psychologist)