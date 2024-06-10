from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    prepopulated_fields = {"slug":('name', )}
    search_fields = ('name', )

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created', 'updated')
    prepopulated_fields = {'slug':('title',)}
    search_fields = ('title', 'category')
    list_filter = ('category', )
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    readonly_fields = ('created', 'updated')
    
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'email', 'category', 'created', 'updated',)
    list_filter = ('category', )
    search_fields = ('full_name', 'phone', 'email')
    ordering = ('-created',)
    readonly_fields = ('created', 'updated')

class ProjectImagesInline(admin.TabularInline):
    model = ProjectImages

@admin.register(OurProjects)
class OurProjectsAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'client', 'created_date', 'created', 'updated')
    search_fields = ('name', 'title')
    ordering = ('-created_date', )
    readonly_fields = ('created', 'updated')
    inlines = [ProjectImagesInline]