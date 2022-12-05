from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from C_S.models import Country, State
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from C_S.serializers import CountrySerializer, StateSerializer, State2Serializer

def firstfun(request):
    return HttpResponse('hello, world')

class CountryModelViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    
class StateModelViewSet(ModelViewSet):
    serializer_class = State2Serializer
    queryset = State.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = State.objects.all()
        serializer = StateSerializer(queryset, many = True)
        return Response(serializer.data)