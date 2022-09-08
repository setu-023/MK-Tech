from django.urls import path

from order.views.order import *


urlpatterns = [
    
    path('', OrderListCreateAPIView.as_view(), name='order-list-create-api'),
	path('<int:pk>', OrderRetrieveUpdateDestroyAPIView.as_view()), 
    path('status/<int:pk>', OrderStatusUpdateAPIView.as_view()), 

]