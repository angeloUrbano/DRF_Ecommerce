from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from apps.users.api.serializers import  UserSerializers , TestUserSerializers , UserListSerializers
from apps.users.models import User



@api_view(["GET" , "POST"])
def User_Api_View(request):
    if request.method=="GET":
        user = User.objects.all()
        user_serializers = UserListSerializers(user , many=True)

        # test_data= {
        #     "name": "angelo",
        #     "email":"juan@gmai.com"

        # }
        # test_user = TestUserSerializers(data=test_data)
        # if test_user.is_valid():
        #     #test_user.save()
        #     print("paso validaciones")
        # else:
        #     print(test_user.errors)    

        return Response(user_serializers.data , status= status.HTTP_200_OK)
    elif request.method== "POST":
        print(request.data)
        user_serializers = UserSerializers(data = request.data)

        if user_serializers.is_valid():
            user_serializers.save()
            return Response(user_serializers.data , status= status.HTTP_201_CREATED)
        else:
            return Response(user_serializers.errors , status= status.HTTP_400_BAD_REQUEST) 




@api_view(["GET" , "PUT" , "DELETE"])
def User_detail_view(request , pk=None):
    user = User.objects.get(id=pk)
    
    if user :
        if request.method=="GET":

            user_serializers = UserSerializers(user)
            return Response(user_serializers.data , status=status.HTTP_200_OK)

        elif request.method=="PUT":

            user_serializers = UserSerializers(user , data=request.data)
            if user_serializers.is_valid():
                user_serializers.save()
                return Response(user_serializers.data, status=status.HTTP_200_OK)
            else:
                return Response(user_serializers.errors , status= status.HTTP_400_BAD_REQUEST) 

        elif request.method=="DELETE": 

            user.delete()
        return Response({'message':'usuario eliminado correctamente'} , status=status.HTTP_200_OK)
             

