from django.urls import path

from product.views.product import *


urlpatterns = [
    
    path('', ProductListCreateAPIView.as_view(), name='product-list-create-api'),
	path('<int:pk>', ProductRetrieveUpdateDestroyAPIView.as_view()), 
    path('search/', SearchResultsView.as_view()),
]