from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from rest_framework import renderers
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from tourisminfo.models import Country, State, Sightseeings, Transport 
from tourisminfo.serializers import CountrySerializer, StateSerializer, State2Serializer, SightseeingsSerializer, Sightseeigns3Serializer, TransportSerializer, Transport3Serializer


def firstfun(request):
    return HttpResponse('hello, world')

class CountryModelViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    
class StateModelViewSet(ModelViewSet):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = State.objects.all()
        serializer = State2Serializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        user = get_object_or_404(State, pk=pk)
        serializer = State2Serializer(user)
        return Response(serializer.data)

class SightseeingsModelViewSet(ModelViewSet):
    serializer_class = SightseeingsSerializer
    queryset = Sightseeings.objects.all()
    
    def list(self, request, *args, **kwargs):
        queryset = State.objects.all()
        serializer = Sightseeigns3Serializer(queryset, many = True)
        return Response(serializer.data)
        
    def retrieve(self, request, pk=None):
        user = get_object_or_404(Sightseeings, pk=pk)
        serializer = Sightseeigns3Serializer(user)
        return Response(serializer.data)
    
class  TransportModelViewSet(ModelViewSet):
    serializer_class = TransportSerializer
    queryset = Transport.objects.all
    
    def list(self,request, *args, **kwargs):
        queryset = Transport.objects.all()
        serializer = Transport3Serializer(queryset, many = True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk = None):
        user = get_object_or_404(Transport, pk=pk)
        serializer = Transport3Serializer(user)
        return Response(serializer.data)



