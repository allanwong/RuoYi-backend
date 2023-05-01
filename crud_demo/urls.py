from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import CrudDemoModelViewSet

router = SimpleRouter()
router.register("api/crud_demo", CrudDemoModelViewSet)

urlpatterns = [
    path('api/crud_demo/Download/', CrudDemoModelViewSet.as_view({'get': 'Download'})),
]
urlpatterns += router.urls

