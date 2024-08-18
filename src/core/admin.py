from django.contrib import admin
from.models import Product, Package, Category, Customer_review, Additional, Message

admin.site.site_header= "ادارة موقع الكتورن"
admin.site.site_title= "متجرالكترون"

#product admin 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProName', 'ProPrice', 'ProQua', 'Proimg_url')
    search_fields = ('ProName',) 
admin.site.register(Product, ProductAdmin)

#package admin 
class PackageAdmin(admin.ModelAdmin):
    list_display = ('PkName', 'PkPrice', 'PkClicks', 'Pkimg_url')
    search_fields = ('PkName',)
admin.site.register(Package, PackageAdmin)

#customer review admin 
class Customer_reviewAdmin(admin.ModelAdmin):
    list_display= ('CrName', 'CrShow')
    search_fields = ('CrName',)
admin.site.register(Customer_review, Customer_reviewAdmin)

class AdditionalAdmin(admin.ModelAdmin):
    list_display = ('AdName', 'id')    
admin.site.register(Additional, AdditionalAdmin)

#category admin 
admin.site.register(Category)

#message admin 
admin.site.register(Message)