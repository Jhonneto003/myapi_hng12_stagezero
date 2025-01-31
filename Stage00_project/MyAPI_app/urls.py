from django.urls import path
from .views import MyApiView

urlpatterns = [
    path('user-info/', MyApiView.as_view(), name= 'user-info'),

]

