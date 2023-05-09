from django.contrib import admin
from catalogue.models import Main_Directions, Category,Product_card,Product_detailpage,Characteristics,Product_images,Comp_logo
# Register your models here.
admin.site.register(Main_Directions)
admin.site.register(Category)
admin.site.register(Comp_logo)


admin.site.register(Product_card)
admin.site.register(Product_detailpage)
admin.site.register(Characteristics)
admin.site.register(Product_images)