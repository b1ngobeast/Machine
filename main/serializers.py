from rest_framework import serializers
from main.models import Creator


class CreatorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60)
    country = serializers.CharField(max_length=60)

    class Meta:
        model = Creator
        fields = '__all__'


class CreatorsForCountries(serializers.Serializer):  # Обработка создателей при запросе страны
    name = serializers.CharField(max_length=60)


class CountriesSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)

    def get_name(self, lst):
        print(lst)
        queryset = Creator.objects.filter(country=lst)
        return CreatorsForCountries(queryset, many=True).data


class CarSerializer(serializers.Serializer):
    car = serializers.CharField(max_length=60)
    creator = serializers.CharField(max_length=100)
    first_year = serializers.CharField(max_length=4)
    last_year = serializers.CharField(max_length=4)
