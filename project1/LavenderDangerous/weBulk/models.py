from django.db import models

# Create your models here.
class Product(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    name = models.CharField(max_length=200, help_text="Enter Product Name")
    price = models.FloatField(default=None)
    quantity = models.IntegerField(default=None)
    description = TextField(max_length=2000, help_text="Enter Product Description")
    image = CharField(max_length=200, help_text="Enter Image Path")
    category = ManyToManyField(Category, help_text="Select a category for this item")
    

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
		
class Category(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    name = models.CharField(max_length=200, help_text="Enter Product Name")
    product = ManyToManyField(Product, help_text="Select a product for this category")

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
		
class User(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    name = models.CharField(max_length=200, help_text="Enter User Name")
    password-hash = models.CharField(max_length=200)
    shipping-address = models.CharField(max_length=200, help_text="Comma Separated Shipping Address")
    billing-address = models.CharField(max_length=200, help_text="Comma Separated Billing Address")
    account-standing = models.IntegerField(default=0)
    cart = models.OneToOneField(ShoppingCart)
    

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
		
class ShoppingCart(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.OneToOneField(User)
    product = ManyToManyField(Product)
    

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
		
class Review(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    rating = IntegerField(default=None)
    review-text = TextField(max_length=1000,help_text="Enter Product Review")
    

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name
		
class Requests(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    request-title = models.CharField(max_length=200, help_text="Enter Request Title")
    request-text = models.TextField(max_length=200, help_text="Enter Request Text")
    popularity = IntegerField(default=0)
    

    # Metadata
    class Meta: 
        ordering = ["-my_field_name"]

    # Methods
    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the MyModelName object (in Admin site etc.)
        """
        return self.field_name