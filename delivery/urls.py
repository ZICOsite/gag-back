from rest_framework import routers
from delivery.views import Delivery_ViewSet

router = routers.DefaultRouter()

router.register(r'delivery',Delivery_ViewSet,'delivery')


urlpatterns = router.urls
