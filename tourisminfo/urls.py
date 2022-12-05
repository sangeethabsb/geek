from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from tourisminfo.views import CountryModelViewSet,StateModelViewSet, SightseeingsModelViewSet, TransportModelViewSet
router = DefaultRouter()
router.register('country', CountryModelViewSet, "country")
router.register('state', StateModelViewSet, "state")
router.register('sightseeigns', SightseeingsModelViewSet, "sightseeings")
router.register('transport', TransportModelViewSet, "transport")
urlpatterns = [
    path('', views.firstfun)
] + router.urls
