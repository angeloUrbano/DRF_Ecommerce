from apps.products.api.serializer.product_serializers import ProductSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status


from apps.base.api import generalListAPIView


class ProductListAPIView(generalListAPIView):
    serializer_class = ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializers


    def post(self , request):
        print(request)

        producto_serializer = self.serializer_class(data= request.data) 
        if producto_serializer.is_valid():
            producto_serializer.save()
            return Response(producto_serializer.data , status= status.HTTP_201_CREATED)
        else:
            return Response(producto_serializer.errors , status= status.HTTP_400_BAD_REQUEST) 


class ProductRetrieveAPIView(generics.RetrieveAPIView):     
    serializer_class = ProductSerializers 

    def get_queryset(self): 
        return self.get_serializer().Meta.model.objects.filter(estado=True)
          

class ProductDestroyAPIView(generics.DestroyAPIView):     
    serializer_class = ProductSerializers 

    def get_queryset(self): 
        return self.get_serializer().Meta.model.objects.filter(estado=True)
          