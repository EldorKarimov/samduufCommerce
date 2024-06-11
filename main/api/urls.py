from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view()),
    path('services/', views.ServicesListAPIView.as_view()),
    path('services/<slug:cat_slug>/', views.ServicesListAPIView.as_view()),
    path('services/<slug:cat_slug>/<slug:service_slug>/', views.ServicesDetailAPIView.as_view()),
    path('about/', views.AboutAPIView.as_view()),
    path('contact/', views.ContactAPIView.as_view()),
    path('projects/', views.OurProjectsListAPIView.as_view()),
    path('projects/<slug:cat_slug>/', views.OurProjectsListAPIView.as_view()),
    path('projects/<slug:cat_slug>/<slug:project_slug>/', views.OurProjectDetailAPIView.as_view()),
]