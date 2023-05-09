from rest_framework import routers
from vacancies.views import Jobs_ViewSet

router = routers.DefaultRouter()

router.register(r'jobs',Jobs_ViewSet,'jobs')
urlpatterns = router.urls
