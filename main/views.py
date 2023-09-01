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
        lst = Creator.objects.all()
        return Response(CreatorSerializer(lst, many=True).data)

    def post(self, request, *args, **kwargs):
        serializer = CreatorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


class CountryAPIView(APIView):

    def get(self, request):
        query_params = request.query_params

        name = query_params.get('name', None)
        if name is None:
            return Response({'error': 'No name provided'})

        lst = Creator.objects.filter(country=name)
        return Response(CreatorSerializer(lst, many=True).data)
