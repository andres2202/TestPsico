from rest_framework import serializers
from psicoApp.models.psychologist import Psychologist
from psicoApp.models.account import Account
from psicoApp.models.city import City
from psicoApp.models.type_specialty import TypeSpecialty
from .accountSerializer import AccountSerializer
from .citySerializer import CitySerializer
from .typeSpecialtySerializer import TypeSpecialtySerializer

class PsychologistSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    city = CitySerializer()
    type_specialty = TypeSpecialtySerializer()
    class Meta:
        model = Psychologist
        fields  = '__all__'

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        cityData = validated_data.pop('city')
        typeSpecialtyData = validated_data.pop('typeSpecialty')
        psychologistInstance = Psychologist.objects.create(**validated_data)
        Account.objects.create(user=psychologistInstance, **accountData)
        City.objects.create(user=psychologistInstance, **cityData)
        TypeSpecialty.objects.create(user=psychologistInstance, **typeSpecialtyData)
        return psychologistInstance

    def to_representation(self,obj):
        psychologist = Psychologist.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        city = City.objects.get(user=obj.id)
        TypeSpecialty = TypeSpecialty.objects.get(user=obj.id)

        return {
            'id': psychologist.id_document,
            'username': psychologist.username,
            'name': psychologist.name,
            'email': psychologist.email,
            'city': {
                'id': city.id,  
                'name': city.name
            }
            'address': psychologist.address,
            'phone': psychologist.phone,
            'typeSpecialty':{
                'id': typeSpecialty.id_specialty,
                'name': typeSpecialty.nameSpecialty
            }
            'description': psychologist.description,
            'gender': psychologist.gender,
            'price': psychologist.price,
            'account': {
                'id': account.id,
                'isActive': account.isActive
            }
        }



