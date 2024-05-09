from django.db import models

# Models

class Category(models.Model):
    """A category model that includes a name and a friendly name."""
    # fix spelling error in admin panel
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=254)
    # add a friendly name field to the category model, that is optional
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

# string methods
    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
    
class Product(models.Model):
    """A product model that includes a name, description, price, category, and image."""
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    # to understand the concept
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name    
