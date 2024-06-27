from django.shortcuts import render
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from ..models import Product
from ..serializers.serializers import ProductSerializer, ProductSerachRequestSeriailizer
from django.db.models import Q, Sum, Count, Avg
from rest_framework.parsers import MultiPartParser

from django.core.mail import send_mail


@api_view(['GET'])
def index(request):
    products = Product.objects.filter()
    ser = ProductSerializer(products, many= True)
    return Response(ser.data)

@api_view(['POST'])
@parser_classes([MultiPartParser])
def create(request):
    reqSer = ProductSerializer(data= request.data)
    if reqSer.is_valid():
        reqSer.save()
        return Response(reqSer.data, status= status.HTTP_201_CREATED)
    return Response(reqSer.errors ,status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def search(request):
    reqSer = ProductSerachRequestSeriailizer(data= request.data)
    if reqSer.is_valid():
        data = reqSer.validated_data
        products = Product.objects.filter(
            name__icontains = data['name']
        )
        
        if data['category']:
            products= products.filter(
                category = data['category']
            )
        
        if data['price_from'] > 0 and data['price_to'] == 0 :
            products = products.filter(
                price__gte = data['price_from']
            )
        elif data['price_from'] >= 0 and data['price_to'] > 0 :
            products = products.filter(
                price__range = (data['price_from'], data['price_to'])
            )
            
        if data['is_date']:
            products = products.filter(
                created_at__date__range = (data['date_from'], data['date_to'])
            )
        count = products.count()
        responseSer = ProductSerializer(products, many= True)
        return Response({
            "count": count,
            "data": responseSer.data
        })
    return Response(reqSer.errors ,status= status.HTTP_400_BAD_REQUEST)


def temp(request):
    """ for i in range(70):
        send_mail(
            "Subject here",
            "Here is the message.",
            "samerhd3@gmail.com",
            ["ferasaljabry@gmail.com"],
            fail_silently=False,
        ) """
    return render(request, 'index.html', {
        "name": "sdfs",
        "products": [
            {
                "id": 1,
                "name": "p1"
            },
            {
                "id": 1,
                "name": "p2"
            },
            {
                "id": 1,
                "name": "p3"
            },
            {
                "id": 1,
                "name": "p4"
            },
        ]
    })