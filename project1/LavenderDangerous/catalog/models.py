from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

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
         return reverse('product-detail', args=[str(self.id)])

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

    def display_price(self):
        """
        Returns price
        """
        return self.price


class Profile(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    user = models.OneToOneField(User, default=None, on_delete=models.CASCADE)
    shipping_address = models.CharField(max_length=200, help_text="Comma Separated Shipping Address")
    billing_address = models.CharField(max_length=200, help_text="Comma Separated Billing Address")
    account_standing = models.IntegerField(default=0)

    # Metadata
    class Meta:
        pass
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
        return self.user.first_name +" "+ self.user.last_name 
        
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class ShoppingCart(models.Model):
    """
    A typical class defining a model, derived from the Model class.
    """
    user = models.ForeignKey(User, default=None)
    product = models.ForeignKey(Product, default=None, blank=True)
    quantity = models.IntegerField(default=0)

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
        return self.user.first_name

    def display_product(self):
        return self.product.name

    def display_genre(self):
        return ', '.join([ product.name for product in self.product.all()[:3] ])

    display_product.short_description = 'Products'

    def display_user(self):
        return self.user.first_name

    display_user.short_description = 'User'

    def display_quantity(self):
        """
        Creates a string for quantity of a product
        """
        return self.quantity

    number_items = property(display_quantity)


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
        return self.user.first_name
    display_user.short_description = 'User'

    def display_rating(self):
        return self.rating


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
        return self.user.first_name
    display_user.short_description = 'User'
