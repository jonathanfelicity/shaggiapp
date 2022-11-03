from django.urls import path 


from .views import *



urlpatterns = [

    path('', home, name='home'),
    path('exchange/', exchange, name='exchange'),
    path('chart/', chart, name='chart'),
    path('converter/', converter, name='converter'),
    path('contact/', contacts, name='contact'),






    # 
]