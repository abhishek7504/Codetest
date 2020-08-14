from rest_framework import serializers
from .models import User,GlobalConacts
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','name','phone_number','email','password']
        read_only_fields = ['id']


class UserLoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length = 15,required = True)
    password = serializers.CharField(max_length = 20,required=True)


class AuthUserSerializer(serializers.ModelSerializer):
    auth_token = serializers.SerializerMethodField()




class GlobalConactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalConacts
        fields = '__all__'