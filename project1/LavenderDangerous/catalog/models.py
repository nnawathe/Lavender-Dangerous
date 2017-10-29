from django.db import models

# Create your models here.

import uuid # Required for unique products

class Category(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    name = models.CharField(max_length=200, help_text="Enter Product Name")

    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('category', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name

class Product(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular product")
    name = models.CharField(max_length=200, help_text="Enter Product Name")
    price = models.FloatField(default=None)
    quantity = models.IntegerField(default=None)
    description = models.TextField(max_length=2000, help_text="Enter Product Description")
    category = models.ManyToManyField(Category, help_text="Select a category")
    image = models.CharField(max_length=200, help_text="Enter Image Path")


    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('product', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
        
    def display_category(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ category.name for category in self.category.all()[:3] ])
    display_category.short_description = 'Category'
    
class ShoppingCart(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular product")
    product = models.ManyToManyField(Product)
    

    # Metadata
    class Meta: 
        ordering = ["user"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('cart', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.user + self.cart
        
    def get_product():
        return "\n".join([p.products for p in self.product.all()])
		
class User(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    name = models.CharField(max_length=200, help_text="Enter User Name")
    email = models.CharField(max_length=200, unique=True, help_text="Enter Email Address")
    password_hash = models.CharField(max_length=200)
    shipping_address = models.CharField(max_length=200, help_text="Comma Separated Shipping Address")
    billing_address = models.CharField(max_length=200, help_text="Comma Separated Billing Address")
    account_standing = models.IntegerField(default=0)
    cart = models.OneToOneField(ShoppingCart,default=None)

    # Metadata
    class Meta: 
        ordering = ["name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('account', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.name
		
		
class Review(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rating = models.IntegerField(default=None)
    review_text = models.TextField(max_length=1000,help_text="Enter Product Review")
    

    # Metadata
    class Meta: 
        ordering = ["product"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('review', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.review_text
        
    def display_user(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ user.name for user in self.user.all()[:3] ])
    display_user.short_description = 'User'
		
class Request(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    request_title = models.CharField(max_length=200, help_text="Enter Request Title")
    request_text = models.TextField(max_length=200, help_text="Enter Request Text")
    popularity = models.IntegerField(default=0)
    

    # Metadata
    class Meta: 
        ordering = ["request_title"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('request', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.request_title
    
    def display_user(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ user.name for user in self.user.all()[:3] ])
    display_user.short_description = 'User'
        
