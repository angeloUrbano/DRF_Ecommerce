from apps.base.api import generalListAPIView
from apps.products.api.serializer.generalserializers import MeasureUnitSerializer, CategoryProductSerializer , IndicadorSerializer

class MeasureUnitListAPIView(generalListAPIView):
    serializer_class = MeasureUnitSerializer


class CategoryProductListAPIView(generalListAPIView):
    serializer_class = CategoryProductSerializer


class IndicadorListAPIView(generalListAPIView):
    serializer_class = IndicadorSerializer

  
            
    