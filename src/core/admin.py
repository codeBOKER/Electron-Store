from django.contrib import admin
from.models import Product, Package, Category, Customer_review, Additional


#product admin 
class ProductAdmin(admin.ModelAdmin):
    list_display = ('ProName', 'ProPrice', 'ProQua', 'ProClicks')
    search_fields = ('ProName',)
admin.site.register(Product, ProductAdmin)

#package admin 
class PackageAdmin(admin.ModelAdmin):
    list_display = ('PkName', 'PkPrice', 'PkClicks')
    search_fields = ('PkName',)
admin.site.register(Package, PackageAdmin)

#customer review admin 
class Customer_reviewAdmin(admin.ModelAdmin):
    list_display= ('CrName', 'CrShow')
    search_fields = ('CrName',)
admin.site.register(Customer_review, Customer_reviewAdmin)

#category admin 
admin.site.register(Category)

admin.site.register(Additional)


