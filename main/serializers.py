from rest_framework import serializers
from main.models import Creator, Car


class CountryForCreator(serializers.Serializer):  #При запросе производителя добавлять страну
    country = serializers.CharField(max_length=60)


class CarForCreator(serializers.Serializer):  #При запросе производителя добавлять авто
    car = serializers.CharField()

class CreatorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60)

    def get_country(self, lst):
        queryset = Creator.objects.filter(name=lst)
        return CountryForCreator(queryset, many=True).data
  #Dont work now
    # def get_car(self, lst):
    #     queryset = Car.objects.filter(name=lst)
    #     return CarForCreator(queryset, many=True).data



    class Meta:
        model = Creator
        fields = '__all__'


class CreatorForCountry(serializers.Serializer):  # Обработка создателей при запросе страны
    name = serializers.CharField(max_length=60)


class CountrySerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)

    def get_name(self, lst):
        queryset = Creator.objects.filter(country=lst)
        return CreatorForCountry(queryset, many=True).data


class CarSerializer(serializers.Serializer):
    car = serializers.CharField(max_length=60)
    creator = serializers.CharField(max_length=100)
    first_year = serializers.CharField(max_length=4)
    last_year = serializers.CharField(max_length=4)
