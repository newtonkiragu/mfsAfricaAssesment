from rest_framework.routers import DefaultRouter

from api.views import PointsViewSet

router = DefaultRouter()
router.register(r'points', PointsViewSet, basename='points')
urlpatterns = router.urls
