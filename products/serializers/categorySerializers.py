from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from ..models import Category, Product 
from .serializers import ProductSerializer

class CategoryModelSerializer(serializers.ModelSerializer):
    name1 = serializers.SerializerMethodField()
    
    def get_name1(self, obj):
        return "hello "+ obj.name
    
    class Meta:
        model = Category
        fields= ['id', 'name', 'note', 'name1']
        
class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField(read_only= True)
    name= serializers.CharField(
        max_length= 250,
        validators = [
            UniqueValidator(queryset= Category.objects.all())
        ]
    )
    note = serializers.CharField(
        max_length= 500, write_only= True,
        allow_blank= True,
        required= False,
        default= ""
    )
    products = ProductSerializer(many= True)
    
    def create(self, validated_data):
        return Category.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.note = validated_data.get('note', instance.note)
        instance.save()
        return instance
    
class CategorySearchRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 250, allow_blank= True)
    product_name= serializers.CharField(
        max_length= 250,
        allow_blank= True
    )
    product_price = serializers.DecimalField(
        max_digits= 20,
        decimal_places= 4
    )
    