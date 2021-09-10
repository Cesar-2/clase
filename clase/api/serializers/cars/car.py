from rest_framework import serializers
from ...models import Car, User

class CarSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ['id', 'number_plate','model','branch']

    def get_cars(self):
        return CarSerializer(Car.objects.all(),many=True).data
    
  