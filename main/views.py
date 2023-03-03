from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import *


@api_view(['GET'])
def company(request):
    company = Company.objects.last()
    return Response(CompanySerializer(company).data)


@api_view(['GET'])
def company_text(request):
    company_text = Company_text.objects.last()
    return Response(Company_textSerializer(company_text).data)


@api_view(['POST'])
def buyurtma(request):
    name = request.POST.get('name')
    phone = request.POST.get('phone')
    Buyurtma.objects.create(
        name=name,
        phone=phone,
    )
    return Response('Success')


@api_view(['GET'])
def sales_price(request):
    sales_price = Sales_price.objects.last()
    return Response(Sales_priceSerializer(sales_price).data)


@api_view(['GET'])
def production(request):
    production = Production.objects.all()[:3]
    return Response(ProductionSerializer(production).data)


@api_view(['GET'])
def about_production(request):
    about_production = About_production.objects.all()[:3]
    return Response(About_productionSerializer(about_production).data)


@api_view(['GET'])
def tea(request):
    tea = Tea.objects.last()
    return Response(TeaSerializer(tea).data)


@api_view(['GET'])
def about_company(request):
    about_company = About_company.objects.last()
    return Response(About_companySerializer(about_company).data)


@api_view(['GET'])
def about_tea(request):
    about_tea = About_tea.objects.all()
    return Response(About_teaSerializer(about_tea).data)


@api_view(['GET'])
def faqts_tea(request):
    faqts_tea = Faqts_tea.objects.all()[:4]
    return Response(Faqts_teaSerializer(faqts_tea).data)