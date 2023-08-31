from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict

from .models import Creator, Countries
from .serializers import CreatorSerializer, CountriesSerializer


def mainpage(request):
    data = {
        'tittle': 'Главная страница'
    }
    return render(request, 'main/mainpage.html', data)


class CreatorAPIView(APIView):

    def get(self, request):
        lst = Creator.objects.all()
        return Response({'posts': CreatorSerializer(lst, many=True).data})

    def post(self, request):
        serializer = CreatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        update_post = Creator.objects.create(
            name=request.data['name'],
            country=request.data['country']
        )
        return Response({'post': CreatorSerializer(update_post).data})


class CountriesAPIView(APIView):

    def get(self, request):
        lst = Countries.objects.all()
        return Response({'posts': CountriesSerializer(lst, many=True).data})