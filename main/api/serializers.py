from rest_framework import serializers
from main.models import *
from common.utils import phone_validator
from rest_framework.exceptions import ValidationError

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
            # 'email':{'required':False}
        }
    def validate_phone(self, obj):
        if phone_validator(obj) == 'invalid':
            raise ValidationError({'phone':'phone number is not valid'})
        return obj
    
    def create(self, validated_data):
        Contact.objects.create(
            full_name = validated_data['full_name'],
            phone = validated_data['phone'],
            email = validated_data.get('email', 'null'),
            text = validated_data['text'],
            category = validated_data['category']
        )
        return super().create(validated_data)
    
class ProjectImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectImages
        fields = '__all__'

class OurProjectsSerializer(serializers.ModelSerializer):
    pictures = serializers.SerializerMethodField()
    category = CategorySerializer()

    class Meta:
        model = OurProjects
        fields = ('id', 'name', 'slug', 'title', 'description', 'project_url', 'client', 'created_date', 'category', 'pictures', 'created', 'updated')
    
    def get_pictures(self, obj):
        pictures = ProjectImages.objects.filter(project = obj)
        return ProjectImagesSerializer(pictures, many = True).data
