from django.db import models
import uuid
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length= 250, unique= True)
    note = models.TextField(blank= True, db_column= "description")

    class Meta:
        db_table= "categories"
        
    def __str__(self) -> str:
        return self.name
        
class Product(models.Model):
    id= models.UUIDField(primary_key= True, default= uuid.uuid4, editable= False)
    name= models.CharField(max_length= 250)
    category= models.ForeignKey(
        Category, 
        on_delete = models.DO_NOTHING,
        related_name= "products",
        related_query_name= "product"
    )
    price= models.DecimalField(max_digits= 20, decimal_places= 4)
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now= True)
    image= models.ImageField(upload_to= 'imgs/products', null= True)
    
    class Meta:
        db_table= "prducts"
        
        unique_together =[
            ['name', 'category']
        ]
        
        permissions = (
            ('search_product', 'can search product'),
            ('export_product', "camn export product")
        )

    def __str__(self) -> str:
        return self.name + ' - ' + self.category.name