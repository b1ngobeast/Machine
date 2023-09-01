from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from main.models import Creator
from main.serializers import CreatorSerializer


def mainpage(request):
    data = {
        'tittle': 'Главная страница'
    }
    return render(request, 'main/mainpage.html', data)


class CreatorAPIView(APIView):

    def get(self, request):
        query_params = request.query_params
        creator = query_params.get('name', None)

        if creator is None:
            return Response({'error': 'No name provided'})

        lst = Creator.objects.filter(name=creator)

        if lst.count() == 0:
            return Response({'error': "name not found"})
        else:
            return Response(CreatorSerializer(lst, many=True).data)

    def post(self, request):
        serializer = CreatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CountryAPIView(APIView):

    def get(self, request):  # Если надо, сделать несколько стран в одном запросе, пока этого функционала нет
        query_params = request.query_params

        name = query_params.get('name', None)
        if name is None:
            return Response({'error': 'No name provided'})

        lst = Creator.objects.filter(country=name)

        if lst.count() == 0:
            return Response({'error': 'Country not found'})
        else:
            return Response(CreatorSerializer(lst, many=True).data)
