from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from .models import Info
from .serializer import InfoSerializer
@api_view(['GET','POST'])
def new(request,file_name,chat_id,message_id):
     Info.objects.create(file_name=file_name,chat_id=chat_id,message_id=message_id)
     return Response({"status":":)"},status=status.HTTP_201_CREATED)
class Search(APIView):
     def get(self,request,file_name):
          malumot=Info.objects.filter(file_name=file_name)
          serializer=InfoSerializer(malumot)
          return Response(serializer.data,status=status.HTTP_200_OK)