from django.conf import settings

from rest_framework.exceptions import MethodNotAllowed
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

import jwt

from customer.serializers import CustomerSerializer
from customer.models import Customer


class CustomerListCreateAPIView(ListCreateAPIView):
    serializer_class = CustomerSerializer
    queryset = Customer.objects.filter()

    def get_permissions(self):
      
        if self.request.method == 'GET':
            return (permissions.IsAdminUser(),)
    
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)
        

    def create(self, request, *args, **kwargs):

        try:
            user = Customer.objects.create_user(
                first_name=self.request.data['first_name'],
                last_name=self.request.data['last_name'],
                gender=self.request.data.get('gender', 'male'),
                email=self.request.data['email'],
                password=self.request.data['password'],
            )
            serializer = self.get_serializer(user)
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(e)
            return Response(data={'message': f'cannot create user. reason: {e}'}, status=status.HTTP_409_CONFLICT)


    def list(self, request, *args, **kwargs):
        
        queryset = self.get_queryset()
        serializer = CustomerSerializer(queryset, many=True)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 


