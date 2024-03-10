from django.urls import path

from apps.products.api.views.general_view import *

from apps.products.api.views.product_views import *


urlpatterns = [
    path('measure_unit/' , MeasureUnitListAPIView.as_view() , name='measure_unit'),
    path('categoryproduct/' , CategoryProductListAPIView.as_view() , name='categoryproduct'),
    path('indicador/' , IndicadorListAPIView.as_view() , name='indicator'),
    path('product/' , ProductListAPIView.as_view() , name='product'),
    path('productcreate/' , ProductCreateAPIView.as_view() , name='productcreate'),
    path('productretrive/<int:pk>' , ProductRetrieveAPIView.as_view() , name='productretrive'),
    path('productdestroy/<int:pk>' , ProductDestroyAPIView.as_view() , name='productdestroy'),
]
