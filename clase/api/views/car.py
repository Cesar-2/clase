from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers import CarSerializer


class CarApi(APIView):
    def get(self, request):
        serializer = CarSerializer()
        cars = serializer.get_cars()    
        return Response(
            {
                'data':cars
            }, status=status.HTTP_200_OK)
    