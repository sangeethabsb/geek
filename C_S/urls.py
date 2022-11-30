from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from C_S.views import CountryModelViewSet, StateModelViewSet
router = DefaultRouter()
router.register('country', CountryModelViewSet, "country")
router.register('state', StateModelViewSet, "state")

urlpatterns = [
    path('', views.firstfun, name = 'firstfun'),
] + router.urls
