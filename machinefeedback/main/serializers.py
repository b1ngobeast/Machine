from rest_framework import serializers
from .models import Creator, Car, Countries, Comment


class CreatorSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)


  #Serializer for CountriesSerializer
class CreatorsForCountries(serializers.Serializer):
    country = serializers.CharField()

class CountriesSerializer(serializers.Serializer):
    def get_name(name):
        queryset = Creator.objects.filter(country=name)
        return CreatorsForCountries(queryset, many=True).data
    name = serializers.CharField(max_length=60)
    countries = get_name(name)

    class Meta:
        model = Countries
        fields = ['name', 'countries']


class CarSerializer(serializers.Serializer):
    car = serializers.CharField(max_length=60)
    creator = serializers.CharField(max_length=100)
    first_year = serializers.CharField(max_length=4)
    last_year = serializers.CharField(max_length=4)
