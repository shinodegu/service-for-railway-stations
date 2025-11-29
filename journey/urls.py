from django.urls import path, include
from rest_framework import routers
from journey.views import (CrewViewSet, StationViewSet,
                    RouteViewSet, TrainTypeViewSet,
                    TrainViewSet, JourneyViewSet,
                    OrderViewSet, TicketViewSet)


app_name = "journey"

router = routers.DefaultRouter()

router.register("crews", CrewViewSet)
router.register("stations", StationViewSet)
router.register("routes", RouteViewSet)
router.register("trains_types", TrainTypeViewSet)
router.register("trains", TrainViewSet)
router.register("journeys", JourneyViewSet)
router.register("orders", OrderViewSet)
router.register("tickets", TicketViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
