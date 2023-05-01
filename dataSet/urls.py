from rest_framework.routers import SimpleRouter

from .views import DataSetModelViewSet
from django.urls import path

router = SimpleRouter()
router.register("api/dataSet", DataSetModelViewSet)

urlpatterns = [
    path('api/dataSet/Download/', DataSetModelViewSet.as_view({'get': 'Download'})),
]
urlpatterns += router.urls
