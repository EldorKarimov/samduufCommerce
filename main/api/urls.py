from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('services/', views.ServicesListAPIView.as_view()),
    path('about/', views.AboutAPIView.as_view()),
    path('contact/', views.ContactAPIView.as_view()),
    path('projects/', views.OurProjectsListAPIView.as_view()),
]