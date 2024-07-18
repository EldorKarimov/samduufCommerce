from django.db import models
from common.models import BaseModel
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator, URLValidator, FileExtensionValidator
from ckeditor_uploader.fields import RichTextUploadingField

class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("name"))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_("slug"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class Services(BaseModel):
    title = models.CharField(max_length=255, verbose_name=_("title"))
    slug = models.SlugField(max_length=255, unique=True, verbose_name=_("slug"))
    short_description = RichTextUploadingField(verbose_name=_("short description"))
    image = models.ImageField(upload_to='media/services/images', verbose_name=_("image"))
    description = RichTextUploadingField(verbose_name=_("description"))
    icon = models.CharField(max_length=50, verbose_name=_("icon"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("category"))

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")

class AdvantagesService(BaseModel):
    name = models.CharField(max_length=255, verbose_name=_("name"))
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="service")

    def __str__(self):
        return self.name

class About(BaseModel):
    name = models.CharField(max_length=150, verbose_name=_("name"))
    description = RichTextUploadingField(verbose_name=_("description"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")
    
class Contact(BaseModel):
    full_name = models.CharField(max_length=150, verbose_name=_("full name"))
    phone = models.CharField(max_length=13, null=True, validators=[
        RegexValidator(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$')
    ], verbose_name=_("phone"))
    email = models.EmailField(verbose_name=_("email"), null=True, blank=True)
    text = models.TextField(verbose_name=_("reference text"))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category', verbose_name=_("category"))

    def __str__(self):
        return self.full_name
    
    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
    
class OurProjects(BaseModel):
    name = models.CharField(max_length=50, verbose_name=_("name"))
    title = models.CharField(max_length=150, verbose_name=_("title"))
    slug = models.SlugField(max_length=150, unique=True, verbose_name=_('slug'))
    description = RichTextUploadingField(verbose_name=_("description"))
    project_url = models.URLField(validators=[URLValidator], verbose_name=_("project link"))
    client = models.CharField(max_length=50, verbose_name='client')
    created_date = models.DateField(verbose_name=_('project created date'))
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=_("category"))

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = _("Our project")
        verbose_name_plural = _("Our projects")
    
class ProjectImages(BaseModel):
    image = models.ImageField(_("image"), upload_to='media/project/images', validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg'])
    ])
    project = models.ForeignKey(OurProjects, on_delete=models.CASCADE, verbose_name=_('our projects'))

    def __str__(self):
        return str(self.image.name)
    
    class Meta:
        verbose_name = _("Project image")
        verbose_name_plural = _("Project images")