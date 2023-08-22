from django.urls import path
from .views import (
    home,
    login,
    signup,
    venues,
    logout,
    venuebook,
    order,
    order_cancle,
    change_password,
    
)
app_name = 'myapp'
urlpatterns = [
    path('',home,name='home'),
    path('logindetails',login,name='login'),
    path('signupdetails',signup,name='signup'),
    path('logoutdetails',logout,name='logout'),
    path('venuesdetail',venues,name='venuesdetails'),
    path('venue/book/<id>',venuebook,name='venuebook'),
    path('orders',order,name='orders'),
    path('order/cancle/<id>/', order_cancle, name="Order_Cancle"),
    path('change/password', change_password, name="Change_password")
    
]