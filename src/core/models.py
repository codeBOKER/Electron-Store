"""
This is the only and the main model in Electron project.
Our models has TWO main model (Product, Package) and also customer review.
The TWO has some founctionalties:
add them to cart - put them into category 
"""

from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.translation import gettext_lazy as _ 

# ---------------------------------------main models-----------------------------------------
#product model
class Product(models.Model):
    ProName= models.CharField(_("product name"), max_length=50)
    ProImg= models.ImageField(_("product image"), upload_to=r'media/product_image', height_field=None, width_field=None, max_length=None)
    ProDesc= models.TextField(_("description"))
    ProPrice= models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    ProCatg= models.ForeignKey("Category", verbose_name=_("product category"), on_delete=models.CASCADE)
    ProQua= models.IntegerField(_("quantity"))
    ProClicks= models.IntegerField(_("number of clicks (populer)"), default=0)
    ProCreated_at = models.DateTimeField(default=timezone.now)

    # ProSlug = AutoSlugField(populate_from=f"product-{slugify(ProName)}", unique=True, null=True, blank=True)
    

    def __str__(self):
        return str(self.ProName)
    
    
# package model
class Package(models.Model):
    PkName= models.CharField(_("product name"), max_length=50)
    PkImg= models.ImageField(_("product image"), upload_to=r'media/package_image', height_field=None, width_field=None, max_length=None)
    PkDesc= models.TextField(_("description"))
    PkPrice= models.DecimalField(_("price"), max_digits=5, decimal_places=2)
    PkClicks= models.IntegerField(_("sales"), default=0)
    PkContent= models.ManyToManyField("Product", verbose_name=_("contents"))
    PkCreated_at = models.DateTimeField(default=timezone.now)
         

    def __str__(self):
        return str(self.PkName)
    
# customet review model
class Customer_review(models.Model):
    CrName= models.CharField(_("customer name"), max_length=50)
    CrJob= models.CharField(_("job"), max_length=50)
    CrImg= models.ImageField(_("photo"), upload_to=r'media/customer_photo', height_field=None, width_field=None, max_length=None)
    CrReview= models.TextField(_("customer review"))
    CrShow= models.BooleanField(_("put in the website"))

    def __str__(self):
        return str(self.CrName)
    
# --------------------------------------founcionalty-----------------------------------------
# category model
class Category(models.Model):
    CatName= models.CharField(_("category name"), max_length=50)
    CatImg= models.ImageField(_("category image"), upload_to=r'media/categroy_image', height_field=None, width_field=None, max_length=None)

    class Meta:
        verbose_name = _("category")
        verbose_name_plural = _("categories")

    def __str__(self):
        return str(self.CatName)
    
    # get the details
    def get_absolute_url(self):
        return reverse("category_detail", kwargs={"pk": self.pk})    

# cart model
class Cart(models.Model):
    CtCreated_at = models.DateTimeField(auto_now_add=True)
    CtUpdated_at = models.DateTimeField(auto_now=True)

# store items 
class CartItem(models.Model):
    CiCart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    CiProduct = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    CiPackage = models.ForeignKey(Package, on_delete=models.CASCADE, null=True, blank=True)
    CiQuantity = models.PositiveIntegerField(default=1)
    CiCreated_at = models.DateTimeField(auto_now_add=True)
    CiUpdated_at = models.DateTimeField(auto_now=True)

# additional pages 
class Additional(models.Model):
    AdName= models.CharField(_("name(this will be showing in the page)"), max_length=50)
    AdImg= models.ImageField(_("img"), upload_to='media/additiona', height_field=None, width_field=None, max_length=None)
        
    
    
    def __str__(self):
        return self.AdName
    



    

    


