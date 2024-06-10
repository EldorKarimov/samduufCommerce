from rest_framework import serializers
from main.models import *
from common.utils import phone_validator

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug', 'created', 'updated')
        extra_fields = {
            'created':{'read_only':True},
            'updated':{'read_only':True},
            'id':{'read_only':True},
        }

class ServicesSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = Services
        fields = ('id', 'title', 'slug', 'short_description', 'image', 'description', 'icon', 'category', 'created', 'updated')
        extra_fields = {
            'created':{'read_only':True},
            'updated':{'read_only':True},
            'id':{'read_only':True},
        }

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'name', 'description', 'created', 'updated')
        extra_fields = {
            'created':{'read_only':True},
            'updated':{'read_only':True},
            'id':{'read_only':True},
        }

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = (
            'id',
            'full_name',
            'phone',
            'email',
            'text',
            'category',
            'created',
            'updated',
        )
        extra_fields = {
            'created':{'read_only':True},
            'updated':{'read_only':True},
            'id':{'read_only':True},
        }
    def validate_phone(self, obj):
        if phone_validator(obj) == 'invalid':
            raise ValueError({'error':'phone number is not valid'})

class OurProjectsSerializer(serializers.ModelSerializer):
    images = serializers.SerializerMethodField()
    class Meta:
        model = OurProjects
        fields = ('id', 'name', 'title', 'description', 'project_url', 'client', 'created_date', 'images' 'created', 'updated')

    def get_images(self, obj):
        return ProjectImages.objects.filter(project_id = obj.id)