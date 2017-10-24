from django.db import models

# Create your models here.

import uuid # Required for unique products

class Product(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular product")
    name = models.CharField(max_length=200, help_text="Enter Product Name")
    price = models.FloatField(default=None)
    quantity = models.IntegerField(default=None)
    description = models.TextField(max_length=2000, help_text="Enter Product Description")
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
		
class Category(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    name = models.CharField(max_length=200, help_text="Enter Product Name")
    product = models.ManyToManyField(Product, help_text="Select a product for this category")

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
		
class ShoppingCart(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.OneToOneField(User)
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
		
class Requests(models.Model):
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
         return reverse('requests', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.request_title
        
