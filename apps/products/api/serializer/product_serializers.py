#aqui se van  aguardar solo los serializers
# que estgenn relacionado netamente con los productos 


from apps.products.models import Product
from rest_framework import serializers
from apps.products.api.serializer.generalserializers import MeasureUnitSerializer , CategoryProductSerializer

class ProductSerializers(serializers.ModelSerializer):
    # esto se hace para que no me muestre solo el numero de la relacion de esas dos variables
    #si no qu eme muestre todo
    #measure_unit = MeasureUnitSerializer()
    #categoy_product = CategoryProductSerializer()
    # o se usa el metodo to_representation para redefinir lo que quiero que se muestre

    class Meta:
        model= Product
        exclude =('estado', "create_date" ,  "modified_date" , "delete_date")


    def to_representation(self , intance):
        return {
            'id':intance.id,
            'description':intance.description,
            'image':intance.image if intance.image !='' else '',
            'measure_unit':intance.measure_unit.description,
            'categoy_product':intance.categoy_product.description

        }