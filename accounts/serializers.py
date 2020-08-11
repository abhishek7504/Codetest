from rest_framework import serializers
from .models import User,GlobalConacts

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id','name','phone_number','email','password']
        read_only_fields = ['id']



class GlobalConactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalConacts
        fields = '__all__'