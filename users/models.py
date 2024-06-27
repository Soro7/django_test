from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
import uuid

class User(AbstractBaseUser, PermissionsMixin):
    id= models.UUIDField(
        primary_key= True,
        default= uuid.uuid4,
        editable= False
    )
    
    username= models.EmailField(
        validators=[UnicodeUsernameValidator],
        max_length= 250,
        unique= True
    )
    email= models.EmailField(
        max_length= 250,
        blank= True,
        default= ""
    )
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)

    is_active= models.BooleanField(default= True)
    is_superuser= models.BooleanField(default= False)
    is_staff= models.BooleanField(default= False)
    
    is_dark = models.BooleanField(default= False)
    language= models.CharField(default= 'en', max_length=3)
    
    objects= UserManager()
    USERNAME_FIELD= "username"
    Email_Field= "email"
    REQUIRED_FIELDS= ["first_name", "last_name"]
    
    class Meta:
        db_table= "users"
        
    def __str__(self) -> str:
        return self.username
    
    
    
