from rest_framework.routers import DefaultRouter

from car_app.api.v1.views import CarViewSet

router = DefaultRouter()
router.register("", CarViewSet, basename="car-apis")

app_name = "car_app"

urlpatterns = router.urls
