from .models import User, GlobalConacts
from .serializers import UserSerializer,GlobalConactsSerializer,UserLoginSerializer, AuthUserSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from django.contrib.auth import authenticate, login


class UserList(APIView):
    """
    List all user, or create a new user.
    """
    def get(self, request, format=None):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():

            instance = serializer.save()
            instance.set_password(serializer.validated_data.get('password'))
            instance.save()
            print('instance-password',serializer.validated_data)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MarkAsSpam(APIView):

  def post(self, request):
    if not request.data.get('id'):
      return Response({"message":"Id for the user not passed"}, status=status.HTTP_400_BAD_REQUEST)
    user = GlobalConacts.objects.get(id=request.data.get('id'))
    user.spam = True
    user.save()
    return Response({"message":"Contact has been marked as spam"})

class Search(APIView):

  def get(self,request):
    query = request.GET.get('query')
    print('line1',request.data)
    print('line2',request.GET)
    if query:
      result = GlobalConacts.objects.filter(Q(first_name__icontains = query) | Q(phone1__icontains = query))
      serializer = GlobalConactsSerializer(result,many=True)
      return Response(serializer.data)
    return Response({"message":"Add some get query"})



class Login(APIView):
  
  def post(self, request):
    serializer = UserLoginSerializer(data=request.data)
    if serializer.is_valid():
      phone_number = serializer.validated_data.get('phone_number')
      password = serializer.validated_data.get('password')
      user = authenticate(username = phone_number,password=password)
      print(user)
      if user is not None:
        login(request,user)
        return Response(serializer.data,status = status.HTTP_200_OK)
      else:
        return Response({"message":"User Not Found"},status=status.HTTP_404_NOT_FOUND)

