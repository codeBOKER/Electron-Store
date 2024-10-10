from django.urls import path
from . import views

urlpatterns = [
    # home page
    path('', views.IndexView.as_view()),
    path('home/', views.IndexView.as_view(), name='home'),
    
    # search page
    path('search/', views.search_view, name='search_view'),

    # category page
    path('category/<int:pk>/', views.CategoryDetailView.as_view(), name='category_detail'),

    path('packages/', views.packages_veiw, name='packages'), # packages
    path('new-items/', views.new_items, name='new_items'), # new items
    path('populer-items/', views.populer_items, name='populer_items'), # populer items

    # cart with its founctions
    path('cart/', views.cart, name='cart'),
    # inside cart page
    path('get-cart-item-count/', views.get_cart_item_count, name='get_cart_item_count'),
    path('update-cart/<int:item_id>/', views.update_cart, name='update_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    # outside cart page
    path('add-to-cart/product/<int:product_id>/', views.add_product_to_cart, name='add_product_to_cart'),
    path('add-to-cart/package/<int:package_id>/', views.add_package_to_cart, name='add_package_to_cart'),   
]