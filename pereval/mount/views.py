from rest_framework import viewsets, status
from .serializers import *
from .models import *
from rest_framework.response import Response


class UsersViewset(viewsets.ModelViewSet):
   queryset = Users.objects.all()
   serializer_class = UsersSerializer

class CoordsViewset(viewsets.ModelViewSet):
   queryset = Coords.objects.all()
   serializer_class = CoordsSerializer


class LevelViewset(viewsets.ModelViewSet):
   queryset = Level.objects.all()
   serializer_class = LevelSerializer


class ImagesViewset(viewsets.ModelViewSet):
   queryset = Images.objects.all()
   serializer_class = ImagesSerializer


class SubmitData(viewsets.ModelViewSet):
   queryset = Pereval.objects.all()
   serializer_class = PerevalSerializer

   def create(self, request, *args, **kwargs):
      serializer = PerevalSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         return Response({
            'status': status.HTTP_200_OK,
            'message': None,
            'id': serializer.data['id'],
         })
      if status.HTTP_400_BAD_REQUEST:
         return Response({
            'status': status.HTTP_400_BAD_REQUEST,
            'message': 'Bad Request',
            'id': None,
         })
      if status.HTTP_500_INTERNAL_SERVER_ERROR:
         return Response({
            'status': status.HTTP_500_INTERNAL_SERVER_ERROR,
            'message': 'Ошибка подключения к базе данных',
            'id': None,
         })
