from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from cerberus import Validator
from ...serializers import UserSerializer

class UserApi(APIView):
    def post(self, request):
        validator = Validator({
            'name': {'required': True,'type': 'string'},
            'email': {'required': True,'type': 'string'},
            'birth_date': {'required': True,'type': 'string'},
            'car': {'required': True,'type': 'integer'},
        })
        if not validator.validate(request.data):
            return Response({
                'errors':validator.errors,
            },status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer()
        serializer.create(request.data)

        return Response(status=status.HTTP_201_CREATED)

    def get(self, request):
        serializer = UserSerializer()
        users =serializer.get_users()

        return Response(
            {
                'data':users
            }, status=status.HTTP_200_OK)

    def delete(self, request):
        if not request.GET.get('id'):
            return Response({
                'errors':'te mamaste wey manda la id',
            },status=status.HTTP_400_BAD_REQUEST)
            
        serializer = UserSerializer()
        serializer.remove_users(request.GET['id'])
        return Response(status=status.HTTP_200_OK)


