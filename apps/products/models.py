from django.db import models
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords

# Create your models here.


class MeasureUnit(BaseModel):
    description =  models.CharField("Descripcion", max_length=50 , unique=True)
    historical = HistoricalRecords()

    @property
    def _hitory_user(self):
        return self.changed_by

    @ _hitory_user.setter
    def _hitory_user(self , value):
        self.changed_by = value


    def __str__(self):
        return self.description



class CategoryProduct(BaseModel):
    description =  models.CharField("Descripcion", max_length=50 , unique=True , null=False , blank=False)
    historical = HistoricalRecords()

    @property
    def _hitory_user(self):
        return self.changed_by

    @ _hitory_user.setter
    def _hitory_user(self , value):
        self.changed_by = value

    def __str__(self):
        return self.description    


class Indicador(BaseModel):
    discount_value = models.PositiveSmallIntegerField(default=0)
    category_product = models.ForeignKey(CategoryProduct, on_delete=models.CASCADE , verbose_name="Indicador de oferta")
    historical = HistoricalRecords()

    @property
    def _hitory_user(self):
        return self.changed_by

    @ _hitory_user.setter
    def _hitory_user(self , value):
        self.changed_by = value

    def __str__(self):
        return self.discount_value


class Product(BaseModel):
    name =  models.CharField("Nombre de producto", max_length=50 , unique=True , null=False , blank=False)
    description = models.TextField(null=False , blank=False)
    measure_unit =  models.ForeignKey(MeasureUnit, on_delete=models.CASCADE , verbose_name="unidad de medida" , null=True)
    image = models.ImageField(upload_to="products/"  , null=True , blank=True)
    categoy_product =  models.ForeignKey(CategoryProduct, on_delete=models.CASCADE , verbose_name="categoria de producto" , null=True)
    historical = HistoricalRecords()

    @property
    def _hitory_user(self):
        return self.changed_by

    @ _hitory_user.setter
    def _hitory_user(self , value):
        self.changed_by = value
        