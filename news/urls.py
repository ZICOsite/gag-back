from rest_framework import routers
from news.views import New_ViewSet,Detail_page_ViewSet

router = routers.DefaultRouter()

router.register(r'news',New_ViewSet,'news')
router.register(r'detail_page',Detail_page_ViewSet,'detail_page')


urlpatterns = router.urls
