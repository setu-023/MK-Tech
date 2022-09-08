from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from customer.views import *

urlpatterns = [
    
    path('', CustomerListCreateAPIView.as_view(), name='user-list-create-api'),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), 
]