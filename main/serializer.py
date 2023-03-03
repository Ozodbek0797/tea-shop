from rest_framework.serializers import ModelSerializer
from .models import *


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class Company_textSerializer(ModelSerializer):
    class Meta:
        model = Company_text
        fields = '__all__'


class BuyurtmaSerializer(ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = ('name', 'phone')


class Sales_priceSerializer(ModelSerializer):
    class Meta:
        model = Sales_price
        fields = '__all__'


class ProductionSerializer(ModelSerializer):
    class Meta:
        model = Production
        fields = '__all__'


class About_productionSerializer(ModelSerializer):
    class Meta:
        model = About_production
        fields = '__all__'


class TeaSerializer(ModelSerializer):
    class Meta:
        model = Tea
        fields = '__all__'


class About_companySerializer(ModelSerializer):
    class Meta:
        model = About_company
        fields = '__all__'


class About_teaSerializer(ModelSerializer):
    class Meta:
        model = About_tea
        fields = '__all__'


class Faqts_teaSerializer(ModelSerializer):
    class Meta:
        model = Faqts_tea
        fields = '__all__'