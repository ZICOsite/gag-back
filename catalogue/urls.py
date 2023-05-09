from rest_framework import routers
from catalogue.views import Main_Directions_ViewSet,Category_ViewSet,Product_card_ViewSet,Product_detailpage_ViewSet,Company_logo_ViewSet,Characteristics_ViewSet

router = routers.DefaultRouter()

router.register(r'main_directions',Main_Directions_ViewSet,'main_directions')
router.register(r'category',Category_ViewSet,'category')

router.register(r'product_card',Product_card_ViewSet,'product_card')
router.register(r'product_detailpage',Product_detailpage_ViewSet,'product_detailpage')
router.register(r'company_logo',Company_logo_ViewSet,'company_logo')
router.register(r'characteristics',Characteristics_ViewSet,'characteristics')

urlpatterns = router.urls
