from django.urls import path,include
from .views import *

urlpatterns = [
    path('login',login_blog,name='login-blog'),
    path('register',register,name='register'),
    
]