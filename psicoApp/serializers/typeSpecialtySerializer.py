from psicoApp.models.type_specialty import TypeSpecialty
from rest_framework import serializers

class TypeSpecialtySerializer(serializers.ModelSerializer):
    class Meta: 
        model = TypeSpecialty
        fields = '__all__'  