from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import RosconViewSet, TipoRosconListViewSet

router = DefaultRouter()
router.register("roscones", RosconViewSet)
router.register("tipo-roscon", TipoRosconListViewSet)

urlpatterns = [
    path('', include(router.urls))
]
