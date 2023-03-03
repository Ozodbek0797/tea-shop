from django.urls import path
from .views import *

urlpatterns = [
    path('company/', company),
    path('company_text/', company_text),
    path('buyurtma/', buyurtma),
    path('sales_price/', sales_price),
    path('production/', production),
    path('about_production', about_production),
    path('tea/', tea),
    path('about_company', about_company),
    path('about_tea/', about_tea),
    path('faqts_tea/', faqts_tea)
]