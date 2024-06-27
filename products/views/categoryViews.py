from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from ..models import Category
from ..serializers.categorySerializers import (
    CategoryModelSerializer, 
    CategorySerializer,
    CategorySearchRequestSerializer
)
from django.contrib.auth.decorators import permission_required

from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


@swagger_auto_schema(
    method= "GET",
    responses={
        status.HTTP_200_OK: CategorySerializer,
        status.HTTP_401_UNAUTHORIZED: "jhk",
        status.HTTP_400_BAD_REQUEST: "unauthrized"
    },
)
@api_view(['Get'])
@permission_required('products.view_product', raise_exception= True)
def index(request):
    categories = Category.objects.all()
    ser = CategorySerializer(categories, many= True)
    return Response(ser.data)


@api_view(['GET'])
def getById(request, id):
    try:
        category= Category.objects.get(pk= id)
        ser= CategoryModelSerializer(category)
        return Response(data= ser.data)
    except Category.DoesNotExist:
        return Response({
                "message": "does not exists"
            } ,status= status.HTTP_404_NOT_FOUND)
        
@swagger_auto_schema(
    method= "POST",
    request_body= CategorySerializer,
    responses={
        status.HTTP_200_OK: CategorySerializer,
        status.HTTP_401_UNAUTHORIZED: "jhk",
        status.HTTP_400_BAD_REQUEST: "unauthrized"
    }
)
@api_view(['POST'])
def create(request):
    ser= CategorySerializer(data= request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status= status.HTTP_201_CREATED)
    return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
def update(request, id):
    try:
        category = Category.objects.get(pk= id)
        ser= CategoryModelSerializer(data= request.data, instance= category)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status= status.HTTP_200_OK)
        return Response(ser.errors, status= status.HTTP_400_BAD_REQUEST)
    except Category.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete(request, id):
    try:
        category = Category.objects.get(pk= id)
        category.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)
    except Category.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
def search(request):
    reqSer= CategorySearchRequestSerializer(data= request.data)
    if reqSer.is_valid():
        data = reqSer.validated_data
        
        categories = Category.objects.filter(
            name__icontains = data['name'],
            product__name__icontains = data['product_name'],
            product__price__gte = data['product_price']
        )
        
        ser = CategorySerializer(categories, many= True)
        return Response(ser.data)
    return Response(reqSer.errors, status= status.HTTP_400_BAD_REQUEST)