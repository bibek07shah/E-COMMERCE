from django.contrib import admin
from .models import *# Register your models here.'
from django.utils.html import format_html

admin.site.register([OfferProduct,Category,SubCategory,Brand])

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','category','subcategory','brand','mark_price','price','desc','display_image']
    list_display_links=['name']
    list_editable=['desc']
    list_per_page=5
    list_filter=['category','subcategory','brand','price']
    search_fields=['price','name']
    ordering=['id']

    def display_image(self,obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 100px;"/>', obj.image.url)