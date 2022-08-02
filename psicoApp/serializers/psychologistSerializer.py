from rest_framework import serializers
from psicoApp.models.psychologist import Psychologist
from psicoApp.models.city import City
from psicoApp.models.typeSpecialty import TypeSpecialty
from .citySerializer import CitySerializer
from .typeSpecialtySerializer import TypeSpecialtySerializer

class PsychologistSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    typeSpecialty = TypeSpecialtySerializer()
    class Meta:
        model = Psychologist
        fields = ['id', 'username', 'password', 'name', 'email', 'city', 'address', 'phone', 'typeSpecialty', 'description', 'gender', 'consultation_price']
    
    def create(self, validated_data):

        cityData = validated_data.pop('city')
        typeSpecialtyData = validated_data.pop('typeSpecialty')

        cityInstance = City.objects.get(name=cityData.get('name'))
        if cityInstance is None:    
            cityInstance = City.objects.create(**cityData)
        typeInstance = TypeSpecialty.objects.get(nameSpecialty=typeSpecialtyData.get('nameSpecialty'))
        if typeInstance is None:
            typeInstance = TypeSpecialty.objects.create(**typeSpecialtyData)

        psychologistInstance = Psychologist.objects.create(city=cityInstance,typeSpecialty=typeInstance,**validated_data)
        return psychologistInstance

    def to_representation(self,obj):
        if hasattr(obj, 'id'):
            return PsychologistSerializer.create_dict(obj)
        else:
            datas = {}
            for p in obj:
                datas['psychologist '+str(p.id)] = PsychologistSerializer.create_dict(p)
            return datas

    def create_dict(obj):   
        psychologist = Psychologist.objects.get(id=obj.id)
        city = City.objects.get(id_city=psychologist.city_id)
        typeSpecialty = TypeSpecialty.objects.get(id_specialty=psychologist.typeSpecialty_id) 
        return {
                'id': psychologist.id,
                'username': psychologist.username,
                'name': psychologist.name,
                'email': psychologist.email,
                'address': psychologist.address,
                'phone': psychologist.phone,
                'description': psychologist.description,
                'gender': psychologist.gender,
                'price': psychologist.consultation_price,
                'city': {
                    'id_city': city.id_city,
                    'name': city.name
                },
                'typeSpecialty': {
                    'id_specialty': typeSpecialty.id_specialty,
                    'nameSpecialty': typeSpecialty.nameSpecialty
                }
            }



        

    


