from django.urls import path

from apps.users.api.api import *


urlpatterns = [
    path('usuario/' , User_Api_View , name="usuarios_api"),
    path('usuario/<int:pk>' , User_detail_view , name="User_detail_view" ),
    
]
