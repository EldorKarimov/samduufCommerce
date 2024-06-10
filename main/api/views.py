from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError

from main.models import *
from .serializers import *

class CategoryListAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class ServicesListAPIView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesSerializer(services, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)

class AboutAPIView(APIView):
    def get(self, request):
        about = About.objects.all().last()
        serializer = AboutSerializer(about)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class ContactAPIView(APIView):
    def post(self, request):
        data = request.data
        print(data)
        serializer = ContactSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success':True,
                'data':serializer.data
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OurProjectsListAPIView(APIView):
    def get(self, request):
        our_projects = OurProjects.objects.all()
        serializer = OurProjectsSerializer(our_projects, many = True)
        data = {
            'success':True, 
            'data':serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)