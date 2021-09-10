from rest_framework import serializers
from ...models import User,Car

from ..cars import CarSerializer

class UserSerializer(serializers.ModelSerializer):
    car = CarSerializer(read_only = True)
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        validated_data['car']= Car.objects.filter(id=validated_data['car']).first()
        user = User.objects.create(**validated_data).id
        return user

    def get_users(self):
        return UserSerializer(User.objects.all(),many= True).data
    
    def remove_users(self,id):
        User.objects.remove(id = int(id))
    