from django.db import models
from products.models import Product
import uuid

class Sale(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )
    
    total = models.DecimalField(
        max_digits= 20, decimal_places= 4
    )
    quantity= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    is_deleted = models.BooleanField(default= False)
    class Meta:
        db_table= "sales"
        

class SaleProduct(models.Model):
    id = models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )
    
    sale = models.ForeignKey(
        Sale, on_delete= models.DO_NOTHING
    )
    
    product = models.ForeignKey(
        Product, on_delete= models.DO_NOTHING
    )
    
    price = models.DecimalField(max_digits= 20, decimal_places= 4)
    
    class Meta:
        db_table= "sales_products"
        
class accounts(models.Model):
    id= models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )
    
    code= models.CharField(max_length= 30)
    parent = models.ForeignKey(
        'self', on_delete= models.DO_NOTHING,
        null= True
    )
    
    class Meta:
        db_table= 'accounts'