from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, NotFound

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
    def get(self, request, cat_slug = None):
        if cat_slug is not None:
            services = Services.objects.filter(category__slug = cat_slug).order_by('-created')
            if not services.exists():
                raise ValidationError({
                    'success':False,
                    "message":"Service not found",
                })
        else:
            services = Services.objects.all().order_by('-created')
        serializer = ServicesSerializer(services, many = True)
        data = {
            'success': True,
            'data': serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class ServicesDetailAPIView(APIView):
    def get(self, request, cat_slug, service_slug):
        try:
            service = Services.objects.get(category__slug = cat_slug, slug = service_slug)
        except Services.DoesNotExist:
            raise NotFound(detail={
                'success':False,
                'detail':"Not found"
            })
        serializer = ServicesSerializer(service)
        return Response({
            'success':True,
            'data':serializer.data
        }, status=status.HTTP_200_OK)

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
    def get(self, request, cat_slug = None):
        
        if cat_slug is not None:
            our_projects = OurProjects.objects.filter(category__slug = cat_slug).order_by('-created_date')
            if not our_projects.exists():
                raise ValidationError({
                    'success':False,
                    'message':'project not found'
                })
        else:
            our_projects = OurProjects.objects.all().order_by('-created_date')
        serializer = OurProjectsSerializer(our_projects, many = True)
        data = {
            'success':True, 
            'data':serializer.data
        }
        return Response(data=data, status=status.HTTP_200_OK)
    
class OurProjectDetailAPIView(APIView):
    def get(self, request, cat_slug, project_slug):
        try:
            project = OurProjects.objects.get(category__slug = cat_slug, slug = project_slug)
        except OurProjects.DoesNotExist:
            raise NotFound(detail={
                'success': False,
                'detail': "Not found"
            })
        serializer = OurProjectsSerializer(project)
        return Response({
            'success':True,
            'data':serializer.data
        }, status=status.HTTP_200_OK)