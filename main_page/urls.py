from rest_framework import routers
from main_page.views import Main_page_ViewSet

router = routers.DefaultRouter()

router.register(r'main_page',Main_page_ViewSet,'main_page')


urlpatterns = router.urls
