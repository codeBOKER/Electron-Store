from django.shortcuts import render
from .models import Product, Package, Cart, Category, CartItem, Additional, Customer_review
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


#------------------------------our pages-------------------------------
# our index page:    
from django.db.models import Q
def index(request):
    """
    This function handles the rendering of the index page. It retrieves and prepares data for the index page template.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered index page with the necessary data.
    """
    categories = Category.objects.all()
    footer_categories = Category.objects.all()[:3]
    customer_reviews = Customer_review.objects.filter(CrShow=True)[:3]

    products = Product.objects.order_by('-ProClicks')[:20]
    packages = Package.objects.all()[:20]

    return render(request, 'index.html', {
        'categories': categories,
        'products': products,
        'packages': packages,
        'footer_categories': footer_categories,
        'customer_reviews': customer_reviews,
    })
def search_view(request):
    """
    This function handles the rendering of the search results page. It retrieves and prepares data for the search results page template.
    It handles both GET and POST requests. For GET requests, it displays the search page with initial data.
    For POST requests, it retrieves the search query from the request, performs a search in the product and package models,
    and displays the search results along with the initial data.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered search results page with the necessary data.
    """
    footer_categories = Category.objects.all()[:3]
    categories = Category.objects.all()

    query = " "  # we put space if there is no query.  (in template) if it is space we use search as placeholder.
    products = Product.objects.order_by('-ProClicks')[:3]
    packages = Package.objects.order_by('-PkClicks')[:3]
    
    if request.method == 'POST':
        query = request.POST.get('query')
        # search in the product model
        result = Product.objects.filter(Q(ProName__icontains=query) | Q(ProDesc__icontains=query))
        products = list(result) + list(products)  # add the most popular 3 items at the end to get more results
        # search in the package model
        result = Package.objects.filter(Q(PkName__icontains=query) | Q(PkDesc__icontains=query))
        packages = list(result) + list(packages)  # add the most popular 3 items at the end to get more results
        
    return render(request, 'search.html', {
        'query': query,
        'products': products,
        'packages': packages,
        'categories': categories,
        'footer_categories': footer_categories,
    })
    
# cart page  
def cart(request):
    """
    This function handles the rendering of the cart page. It retrieves and prepares data for the cart page template.
    It checks if the user has a cart in the session, and if so, retrieves the cart and its associated cart items.
    If the user does not have a cart, it initializes an empty cart and cart items list.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered cart page with the necessary data. The data includes the user's cart, cart items, and footer categories.
    """
    cart_id = request.session.get('cart_id') # get user cart
    footer_categories= Category.objects.all()[:3]
    # present list of items if he has
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        cart_items = CartItem.objects.filter(CiCart=cart)
    else:
        cart = None
        cart_items = []

    return render(request, 'cart.html', {
        'cart': cart,
        'cart_items': cart_items,
        'footer_categories': footer_categories,
    })

# new items page
def new_items(request):
    """
    This function handles the rendering of the new items page. It retrieves and prepares data for the new items page template.
    It fetches the last 20 added products and packages, along with their associated categories and additional information.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered new items page with the necessary data. The data includes categories, footer categories,
    new products, new packages, and an image related to the new items.
    """
    categories = Category.objects.all()
    footer_categories= Category.objects.all()[:3]

    new_products = Product.objects.order_by('-ProCreated_at')[:90]
    new_packages = Package.objects.order_by('-PkCreated_at')[:90]
    title= "منتجات جديدة"
    img= Additional.objects.get(AdName= title).AdImg
    return render(request, 'new.html', {
        'categories':categories,
        'footer_categories':footer_categories,
        'products': new_products,
        'packages':new_packages,
        'img':img,
    })

# populer items page
def populer_items(request):
    """
    This function handles the rendering of the populer items page. It retrieves and prepares data for the populer items page template.
    It fetches the 90 most clicked products and packages, along with their associated categories and additional information.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered populer items page with the necessary data. The data includes categories, footer categories,
    populer products, populer packages, and an image related to the populer items.
    """
    categories = Category.objects.all()
    footer_categories= Category.objects.all()[:3]

    populer_products = Product.objects.order_by('-ProClicks')[:90]
    populer_packages = Package.objects.order_by('-PkClicks')[:90]
    title= "منتجات شائعة"
    img= img= Additional.objects.get(AdName= title).AdImg
    return render(request, 'populer.html', {
        'categories':categories,
        'footer_categories':footer_categories,
        'products': populer_products,
        'packages':populer_packages,
        'img':img,
    })

# our package page 
def packages_veiw(request):
    """
    This function handles the rendering of the packages page. It retrieves and prepares data for the packages page template.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.

    Returns:
    HttpResponse: The rendered packages page with the necessary data. The data includes all packages, footer categories,
    an image related to the packages, and all categories.
    """
    categories = Category.objects.all()
    footer_categories = Category.objects.all()[:3]
    packages = Package.objects.all()
    title = "حقائب الكترونية"
    img = Additional.objects.get(AdName=title).AdImg

    return render(request, 'package.html', {
        'packages': packages,
        'footer_categories': footer_categories,
        'img': img,
        'categories': categories,
    })

# our categry page
from django.views.generic import DetailView

class CategoryDetailView(DetailView):
    """
    This class-based view is responsible for rendering the category page. It retrieves and prepares data for the category page template.

    Attributes:
    model (Category): The model class representing the category.
    template_name (str): The name of the template file to be used for rendering the category page.

    Methods:
    get_context_data(self, **kwargs):
        This method overrides the default get_context_data method to add additional context data to the template.
        It retrieves the category object, related products, footer categories, and other necessary data.

        Parameters:
        **kwargs (dict): Additional keyword arguments passed to the method.

        Returns:
        dict: A dictionary containing the context data to be used in the template.
    """
    model = Category
    template_name = 'category.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = self.get_object()
        context['products'] = Product.objects.filter(ProCatg=category)
        context['footer_categories'] = Category.objects.all()[:3]
        context['categories'] = Category.objects.all()
        context['title'] = category.CatName
        context['img'] = category.CatImg
        return context
# ----------------------------our founctions in pages---------------------------
# 1- add the product to the card
def add_product_to_cart(request, product_id):
    """
    This function adds a product to the user's cart. It also increments the product's click count.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.
    product_id (int): The unique identifier of the product to be added to the cart.

    Returns:
    JsonResponse: A JSON response indicating whether the product was successfully added to the cart.
    """
    product= Product.objects.get(id=product_id)
    product.ProClicks+= 1
    product.save() #save increasing
    if 'cart_id' in request.session:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id
        
    # check if the item is already added
    cart_item, created = CartItem.objects.get_or_create(CiCart=cart, CiProduct=product)
  
    # if the product has been added to the cart, increase quantity
    if not created:
        cart_item.CiQuantity+= 1
    cart_item.save() # save changes
    
    # retunrn response with jason message
    return JsonResponse({'message': 'item added to cart'})

def add_package_to_cart(request, package_id):
    """
    This function adds a package to the user's cart and increments the package's click count.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.
    package_id (int): The unique identifier of the package to be added to the cart.

    Returns:
    JsonResponse: A JSON response indicating whether the package was successfully added to the cart.
    The response contains a 'message' key with the value 'item added to cart'.
    """
    package = Package.objects.get(id=package_id)
    package.PkClicks += 1
    package.save()  # save increasing

    if 'cart_id' in request.session:
        cart_id = request.session['cart_id']
        cart = Cart.objects.get(id=cart_id)
    else:
        cart = Cart.objects.create()
        request.session['cart_id'] = cart.id

    # check if the item is already added
    cart_item, created = CartItem.objects.get_or_create(CiCart=cart, CiPackage=package)

    # if the package has been added to the cart, increase quantity
    if not created:
        cart_item.CiQuantity += 1
    cart_item.save()  # save changes

    # return response with JSON message
    return JsonResponse({'message': 'item added to cart'})

   
# 2- count items in the cart
def get_cart_item_count(request):
    """
    This function retrieves the count of items in the user's cart.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.
        It should contain a session attribute with a 'cart_id' key, which represents the user's cart.

    Returns:
    JsonResponse: A JSON response containing the count of items in the user's cart.
        The response has a 'cartItemCount' key with the count value.
    """
    cart_id = request.session.get('cart_id')
    # count items in the cart if he has cart 
    if cart_id:
        cart = Cart.objects.get(id=cart_id)
        cart_item_count = CartItem.objects.filter(CiCart=cart).count()
    else:
        cart_item_count = 0 #the do not has cart

    return JsonResponse({'cartItemCount': cart_item_count})


# 3- update quanity in the cart 
@csrf_exempt
def update_cart(request, item_id):
    """
    This function updates the quantity of a specific cart item in the database.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.
        It should be a POST request with a JSON body containing the 'quantity' field.
    item_id (int): The unique identifier of the cart item to be updated.

    Returns:
    JsonResponse: A JSON response indicating the success of the operation.
        The response contains a 'success' key with a boolean value indicating whether the operation was successful.
        If successful, it also contains a 'new_quantity' key with the updated quantity value.
    """
    if request.method == 'POST':
        data = json.loads(request.body)
        quantity = data.get('quantity')  # get the quantity from the request body
        # Update the cart item quantity in the database
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.CiQuantity = quantity
        cart_item.save()
        return JsonResponse({'success': True, 'new_quantity': cart_item.CiQuantity})


# 4- remove item from cart
@csrf_exempt
def remove_from_cart(request, item_id):
    """
    This function removes a specific cart item from the database.

    Parameters:
    request (HttpRequest): The request object containing information about the client's request.
        It should be a POST request.
    item_id (int): The unique identifier of the cart item to be removed.

    Returns:
    JsonResponse: A JSON response indicating the success of the operation.
        The response contains a 'success' key with a boolean value indicating whether the operation was successful.
        If successful, it also contains an 'item_id' key with the removed item's unique identifier.
    """
    if request.method == 'POST':
        # Remove the cart item from the database
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.delete()
        return JsonResponse({'success': True, 'item_id': item_id})
        