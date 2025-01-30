from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import MyApiSerializer
from rest_framework.response import Response
# from.models import User
from rest_framework import exceptions
from django.utils.timezone import now


# Create your views here.
# class MyApiView(APIView):
#     def get(self, request, *args, **kwargs):
#         user_id= kwargs.get('id')

#         try:
#             user= User.objects.get(id=user_id)
#         except User.DoesNotExist:
#             return Response({'error:' 'User not found'}, status=404)

#         data = {
#             'email': User.email,
#             'current_datetime': User.registered_at,
#             'github_url': User.github_url
#         }

#         serializer = MyApiSerializer(data)
#         return Response(serializer.data, status=200)

#     def post(self, request, *args, **kwargs):
#         incoming_data= request.data
#         serializer= MyApiSerializer(data=incoming_data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


class MyApiView2(APIView):
    def get(self, request):
        data = { 
            'email': 'ekpeubonabasi@gmail.com',
            'current_datetime': now().isoformat(),
            'github_url': 'https://github.com/Jhonneto003/myapi_hng12_stagezero.git'
        }
        serializer = MyApiSerializer(data)
        return Response(serializer.data)



        

        
        

