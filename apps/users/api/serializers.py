from rest_framework import serializers
from apps.users.models import User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'

    def create(self , validate_data):
        user = User(**validate_data) 
        user.set_password(validate_data["password"])
        user.save()
        return user

    def update(self , instance , validate_data):
        user = super().update(instance , validate_data)
        user.set_password(validate_data["password"])
        user.save()
        return user       

  





class UserListSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields ='__all__'

    #este es el metodo que fuarda cada uno de los valores que tiene fields
    def to_representation(self , instance):
        #super().to_representation(instance)
        print(instance)
        data= {"id":instance.id , "username":instance.username , "email":instance.email , "password":instance.password}
        return data    

class TestUserSerializers(serializers.Serializer):
    name = serializers.CharField(max_length = 255)
    email = serializers.EmailField()


    def validate_name(self, value):
        if "pedro" in value:
            raise serializers.ValidationError("Error text")
        return value


    def validate_email(self, value):
        if value =="":
            raise serializers.ValidationError("campo vacio en email")
        return value

    def validate(self , data):
        if data["name"] in data["email"]:
            raise serializers.ValidationError("el nombre no puede contener el email")
        return data

    def create(self , validate_data):
        print(validate_data) 
        return User.objects.create(**validate_data)  

    def update(self , instance , validate_data) :
        print("aquis")
        instance.name = validate_data.get("name" , instance.name)
        intance.email = validate_data.get("name" , instance.email)
        instance.save()
        return instance 

    # def save(self):
    #     print(self)  
