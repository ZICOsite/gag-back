from rest_framework import routers
from contacts.views import Contacts_ViewSet

router = routers.DefaultRouter()

router.register(r'contacts',Contacts_ViewSet,'contacts')


urlpatterns = router.urls