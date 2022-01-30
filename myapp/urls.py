from .views import CommonViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', CommonViewSet)
urlpatterns = router.urls
