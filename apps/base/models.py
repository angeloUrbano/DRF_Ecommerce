from django.db import models

# Create your models here.

class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    estado = models.BooleanField(default=True)
    create_date = models.DateField("fecha de creacion ", auto_now=False, auto_now_add=True)
    modified_date = models.DateField("fecha de modificacion", auto_now=True, auto_now_add=False)
    delete_date = models.DateField("fecha de eliminacion", auto_now=True, auto_now_add=False)
