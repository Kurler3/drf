from django.db import models

# Create your models here.
class Product(models.Model):
    # TITLE
    title = models.CharField(max_length=120)
    
    # CONTENT (ALLOWS TO BE EMPTY OR NULL)
    content = models.TextField(blank=True, null=True)
        
    # PRICE
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f" % (float(self.price) * 0.8)