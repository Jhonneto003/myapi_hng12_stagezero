from django.urls import path
from .views import MyApiView2

urlpatterns = [
    path('user-info/', MyApiView2.as_view(), name= 'user-info'),

]

