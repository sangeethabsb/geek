from rest_framework import serializers
from tourisminfo.models import Country, State, Sightseeings, Transport


class CountrySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Country
        fields = '__all__'
        
class StateSerializer(serializers.ModelSerializer):

    class Meta:
        model = State
        fields = '__all__'
        
class State2Serializer(serializers.ModelSerializer):
    country = CountrySerializer(read_only = True)
    
    class Meta:
        model = State
        fields = ('id', 'name', 'capital', 'districts', 'country')
        
class SightseeingsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Sightseeings
        fields = '__all__'
        
class Sightseeings2Serializer(serializers.ModelSerializer):
    state = StateSerializer(read_only = True)
    
    class Meta:
        model = Sightseeings
        fields = ('id', 'name', 'ticketfare', 'state')
        
class Sightseeigns3Serializer(serializers.ModelSerializer):
    state1 = State2Serializer(read_only = True)
    
    class Meta:
        model = Sightseeings
        fields = ('id', 'name', 'ticketfare', 'state1')
        
class TransportSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Transport
        fields = '__all__'
        
class Transport2Serializer(serializers.ModelSerializer):
       sightseeings = SightseeingsSerializer(read_only = True)
       
       class Meta:
           model = Transport
           fields = ('id', 'type', 'vehicle_type', 'name', 'price', 'sightseeigns')
           
class Transport3Serializer(serializers.ModelSerializer):
       sightseeings1 = Sightseeigns3Serializer(read_only = True)
       
       class Meta:
           model = Transport
           fields = ('id', 'type', 'vehicle_type', 'name', 'price', 'sightseeigns1')
           