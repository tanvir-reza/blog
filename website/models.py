from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    name = models.TextField(max_length=250,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    phone2 = models.CharField(max_length=20,blank=True,null=True)
    linkedin = models.CharField(max_length=250,blank=True,null=True)
    facebook = models.CharField(max_length=250,blank=True,null=True)
    twitter = models.CharField(max_length=250,blank=True,null=True)
    youtube = models.CharField(max_length=250,blank=True,null=True)
    email = models.EmailField(max_length=50, blank=True,null=True)
    address = models.TextField(max_length=150,blank=True,null=True)
    opening_hours = models.TextField(blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name = "Site Info"

