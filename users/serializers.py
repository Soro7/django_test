from rest_framework import serializers
from .models import User

class UserSerializer(serializers.Serializer):
    id= serializers.UUIDField(
        read_only= True
    )
    username= serializers.EmailField(
        max_length= 250
    )
    email= serializers.EmailField(
        max_length= 250
    )
    
    first_name = serializers.CharField(
        max_length= 250
    )
    last_name = serializers.CharField(
        max_length= 250
    )
    
    is_active= serializers.BooleanField(default= True)
    is_superuser= serializers.BooleanField(default= False)
    is_staff= serializers.BooleanField(default= False)
    
    is_dark = serializers.BooleanField(default= False)
    language= serializers.CharField(default= 'en', max_length=3)
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    

class ChangePasswordSerializer(serializers.Serializer):
    old_password= serializers.CharField(
        max_length= 250
    )
    new_password= serializers.CharField(
        max_length= 250
    )
    confirm_new_password= serializers.CharField(
        max_length= 250
    )