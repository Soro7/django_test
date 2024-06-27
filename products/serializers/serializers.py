from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from ..models import Category, Product

class CategorySer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'

class ProductSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only= True)
    name = serializers.CharField(max_length= 250)
    category= serializers.PrimaryKeyRelatedField(
        queryset= Category.objects.all()
    )
    category_name= serializers.CharField(source= "category.name", read_only= True)
    category_details= CategorySer(source="category", read_only= True)
    price= serializers.DecimalField(max_digits= 20, decimal_places= 4)
    created_at = serializers.DateTimeField(read_only= True)
    image = serializers.ImageField()
    
    class Meta:
        validators = [
            UniqueTogetherValidator(
                queryset= Product.objects.all(),
                fields= ['name', 'category']
            )
        ]
        
    def create(self, validated_data):
        return Product.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance
    
class ProductSerachRequestSeriailizer(serializers.Serializer):
    name = serializers.CharField(max_length= 250, allow_blank= True)
    category = serializers.PrimaryKeyRelatedField(
        queryset= Category.objects.all(),
        allow_null= True
    )
    price_from= serializers.DecimalField(
        max_digits= 20,
        decimal_places= 4
    )
    price_to= serializers.DecimalField(
        max_digits= 20,
        decimal_places=4
    )
    is_date = serializers.BooleanField()
    date_to= serializers.DateField()
    date_from= serializers.DateField()
    