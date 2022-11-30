from rest_framework import serializers
from C_S.models import Country, State

class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'
        
class StateSerializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only=True)
    class Meta:
        model = State
        fields = ('id', 'name','capital', 'districts', 'country' ) 
    
class State2Serializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'