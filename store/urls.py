from django.urls import path
from . import views

urlpatterns = [
  
    path('dashboard', views.dashboard, name="dashboard"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('shop', views.shop, name="shop"),
    path('shop-single/<int:id>', views.shop_single, name="shop-single"),
    path('my-orders/<int:id>', views.orders, name="my-orders"),
   
]





