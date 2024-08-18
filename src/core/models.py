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
    ProName= models.CharField(_("اسم المنتج"), max_length=50)
    ProImg= models.ImageField(_("صورة محلية"), upload_to=r'product_image',null= True, blank=True)
    Proimg_url = models.URLField(_("رابط الصورة"), blank=True, null=True)
    ProDesc= models.TextField(_("الوصف"))
    ProPrice= models.DecimalField(_("السعر (لن يظهر السعر في الموقع)"), max_digits=5, decimal_places=2, null=True, blank=True)
    ProCatg= models.ForeignKey("Category", verbose_name=_("القسم"), on_delete=models.CASCADE)
    ProQua= models.IntegerField(_("quantity"))
    ProClicks= models.IntegerField(_("عدد الضغطات (يحدد شعبية المنتج)"), default=0)
    ProCreated_at = models.DateTimeField(default=timezone.now)

    def save(self, *args, **kwargs):
        if self.ProImg and not self.Proimg_url:
            # Upload the image to an external service and get the URL
            self.Proimg_url = upload_image_to_external_service(self.ProImg)
            # Remove the local image file if you don't want to keep it
        self.ProImg.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.ProName)
    
    class Meta:
        verbose_name = _("منتج")
        verbose_name_plural = _("المنتجات")
    
    
# package model
class Package(models.Model):
    PkName= models.CharField(_("اسم الحقيبة"), max_length=50)
    PkImg= models.ImageField(_("صورة محلية"), upload_to=r'package_image',null= True, blank=True)
    Pkimg_url = models.URLField(_("رابط صورة عبر الانترنت"), blank=True, null=True)
    PkDesc= models.TextField(_("الوصف"))
    PkPrice= models.DecimalField(_("السعر (لن يظهر السعر في الموقع)"), max_digits=5, decimal_places=2, null=True, blank=True)
    PkClicks= models.IntegerField(_("عدد الضغطات (يحدد شعبية المنتج)"), default=0)
    PkContent= models.ManyToManyField("Product", verbose_name=_("محتويات الحقيبة"))
    PkCreated_at = models.DateTimeField(default=timezone.now)
    
    def save(self, *args, **kwargs):
        if self.PkImg and not self.Pkimg_url:
            # Upload the image to an external service and get the URL
            self.Proimg_url = upload_image_to_external_service(self.PkImg)
            # Remove the local image file if you don't want to keep it
        self.PkImg.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.PkName)
    
    class Meta:
        verbose_name = _("حقية")
        verbose_name_plural = _("حقائب جاهزة")
    
# customet review model
class Customer_review(models.Model):
    CrName= models.CharField(_("اسم العميل"), max_length=50)
    CrJob= models.CharField(_("المسمى الوظيفي"), max_length=50)
    CrImg= models.ImageField(_("صورة العميل"), upload_to=r'customer_photo',)
    CrReview= models.TextField(_("مراجعة العميل"))
    CrShow= models.BooleanField(_("اضافة الى الموقع\n(يجب اختيار اكثر من 3)"))

    def __str__(self):
        return str(self.CrName)
    
    class Meta:
        verbose_name = _("مراجعة عميل")
        verbose_name_plural = _("مراجعة العملاء")
    
# --------------------------------------founcionalty-----------------------------------------
# category model
class Category(models.Model):
    CatName= models.CharField(_("اسم القسم"), max_length=50)
    CatImg= models.ImageField(_("صورة القسم"), upload_to=r'category_image',)
    Catimg_url = models.URLField(_("اضافة صورة من الانترنت"), blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.CatImg and not self.Catimg_url:
            # Upload the image to an external service and get the URL
            self.Catimg_url = upload_image_to_external_service(self.CatImg)
            # Remove the local image file if you don't want to keep it
        self.CatImg.delete(save=False)
        super().save(*args, **kwargs)


    class Meta:
        verbose_name = _("قسم")
        verbose_name_plural = _("الاقسام")

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
    AdName= models.CharField(_("اسم الصفحة"), max_length=50)
    AdImg= models.ImageField(_("الصورة"), upload_to=r'addtional_image', null=True, blank=True)
    Adimg_url = models.URLField(_("صورة عبر الانترنت"), blank=True, null=True)        
    
    def save(self, *args, **kwargs):
        if self.AdImg and not self.Adimg_url:
            # Upload the image to an external service and get the URL
            self.Adimg_url = upload_image_to_external_service(self.AdImg)
            # Remove the local image file if you don't want to keep it
        self.AdImg.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.AdName

    class Meta:
        verbose_name = _("صفحت")
        verbose_name_plural = _("صفحات اضافية (الجديد و الشائعة)")

class Message(models.Model):
    head_message= models.TextField(_("رائس الرسالة"))
    footer_message= models.TextField(_("ذيل الرسالة"))
    

    class Meta:
        verbose_name = _("رسالة الوتس")
        verbose_name_plural = _("رسالة الوتس")

    def __str__(self):
        return self.head_message


# upload images function
# import libraries that we need 
import requests
import base64
from django.conf import settings

def upload_image_to_external_service(image):
    KEY = settings.API_KEY 
    url = 'https://api.imgbb.com/1/upload'
    image_data = image.read()
    encoded_image = base64.b64encode(image_data).decode('utf-8')
    payload = {
        'key': KEY,
        'image': encoded_image,  # Base64 encoded image
    }
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        return response.json().get('data', {}).get('url')
    else: return 'فشل تحميل الصورة (يجب حذف هذا النص قبل الحفظ)'
    



