from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.TextField(max_length=200,blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(max_length=50, blank=True,null=True)
    address = models.TextField(max_length=150,blank=True,null=True)

    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name = "Site Info"