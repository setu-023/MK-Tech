from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('customers/', include('customer.urls')),
    path('products/', include('product.urls')),
    path('orders/', include('order.urls')),

]
