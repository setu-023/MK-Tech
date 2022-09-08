from functools import partial
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions, status
from rest_framework.response import Response
import json 

from product.models import Product
from product.serializers import ProductSerializer


class ProductListCreateAPIView(ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def get_permissions(self):
        if self.request.method == 'POST':
            return (permissions.IsAdminUser(),)

        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)

    def create(self, request, *args, **kwargs):

        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'201', 'msg': 'created successfully', 'data':serializer.data, }, status.HTTP_201_CREATED,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  
       
    def list(self, request):

        queryset = self.get_queryset()
        serializer = ProductSerializer(queryset, many=True)
        return Response({ "response": status.HTTP_200_OK,"message":"showing data","data":serializer.data}) 


class ProductRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'

    def get_permissions(self):
        if self.request.method == 'PUT' or self.request.method == 'PATCH' or self.request.method == 'DELETE':
            return (permissions.IsAdminUser(),)
        elif self.request.method == 'GET':
            return (permissions.AllowAny(),)

    def get(self, request, pk, *args, **kwargs):
        try:
            product              = Product.objects.get(id=pk)
            serializer           = ProductSerializer(product)
            product              = serializer.data['images']
        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)
   
    def put(self,request,pk,format=None):

        try:
            product        = Product.objects.get(id=pk)
            ## converting images field to str
            request.data['images'] = str(request.data['images'])
            serializer  = ProductSerializer(product, data=request.data, partial = True)

        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        if serializer.is_valid():
            serializer.save()
            return Response({'status':'200', 'msg': 'data updated', 'data':serializer.data, }, status.HTTP_200_OK,)
        return Response({'status':'400', 'msg': 'Please Insert Correct value', 'data':serializer.errors, }, status.HTTP_400_BAD_REQUEST,)  


    def delete(self,request,pk,format=None):
        try:
            product        = Product.objects.get(id=pk)
        except Exception as e:
            return Response({'status':'404', 'msg': str(e) }, status.HTTP_404_NOT_FOUND,)  

        product.delete()
        return Response({'status':'200', 'msg': 'data deleted', }, status.HTTP_200_OK,)


class SearchResultsView(ListCreateAPIView):

    def get_permissions(self):

        if self.request.method == 'GET':
            return (permissions.AllowAny(),)

    def list(self, request, *args, **kwargs):

        query = self.request.GET.get("q")
        
        product              = Product.objects.filter(name__icontains = query)
        if not product:
            return Response({'status':'404', 'msg': 'no data found' }, status.HTTP_404_NOT_FOUND,)  

        serializer           = ProductSerializer(product, many = True)
        return Response({'status':'200', 'msg': 'showing data', 'data':serializer.data, }, status.HTTP_200_OK,)

   