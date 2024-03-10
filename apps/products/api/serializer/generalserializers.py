from apps.products.models import MeasureUnit , CategoryProduct, Indicador
from rest_framework import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = MeasureUnit
        exclude =('estado', "create_date" ,  "modified_date" , "delete_date")


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude =('estado', "create_date" ,  "modified_date" , "delete_date")


class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude= ('estado', "create_date" ,  "modified_date" , "delete_date")