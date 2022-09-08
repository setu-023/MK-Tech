import email
from functools import partial
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response

from order.models import Order
from order.serializers import OrderSerializer
from customer.models import Customer


class OrderListCreateAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.IsAuthenticated(),)

        elif self.request.method == 'GET':
            return (permissions.IsAdminUser(),)

    def create(self, request, *args, **kwargs):

        request.data['customer_id'] = Customer.objects.get(email=request.user).id
        serializer = OrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  
       
    def list(self, request):

        queryset = self.get_queryset()
        serializer = OrderSerializer(queryset, many=True)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 


class OrderRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            return (permissions.IsAdminUser(),)
        elif self.request.method == 'GET':
            return (permissions.IsAuthenticated(),)

    def get(self, request, pk, *args, **kwargs):
        try:
            order              = Order.objects.get(id=pk)
        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  
        
        get_customer = Customer.objects.get(email=request.user)
        print(get_customer.id, order.customer_id.id)
        if order.customer_id.id == get_customer.id or get_customer.is_superuser:
            serializer         = OrderSerializer(order)
            return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
        return Response({'status':'403', 'msg': 'You do not have permission to perform this action.', }, status.HTTP_403_FORBIDDEN,)

    def put(self,request,pk,format=None):

        try:
            order        = Order.objects.get(id=pk)
            serializer   = OrderSerializer(order, data=request.data, partial = True)

        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'data updated', 'data':serializer.data, }, status.HTTP_200_OK,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  


    def delete(self,request,pk,format=None):
        try:
            order        = Order.objects.get(id=pk)
        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        order.delete()
        return Response({'status':'200', 'msg': 'data deleted', }, status.HTTP_200_OK,)



class OrderStatusUpdateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()

    def get_permissions(self):
        if self.request.method == 'PUT':
            return (permissions.IsAdminUser(),)

    def put(self,request,pk,format=None):

        try:
            order        = Order.objects.get(id=pk)
            serializer   = OrderSerializer(order, data=request.data, partial = True)

        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'data updated', 'data':serializer.data, }, status.HTTP_200_OK,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  
