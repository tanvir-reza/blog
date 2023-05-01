from django.db import models
from ckeditor.fields import RichTextField
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files import File
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
PEOPLE_CHOICES = (
    ('advisor','Advisor'),
    ('research_assistant', 'Research Assistant'),
    ('research_student','Research Student'),
)

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO() 
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=50) 
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class HomeSlider (models.Model):
    title = models.CharField(max_length=200, blank = True)
    slogan = models.CharField(max_length=200, blank = True)
    Details = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='HomeSlider/', blank = False)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)

       #for compress images
    def save(self, *args, **kwargs):
       # call the compress function
        new_image = compress(self.photo)
        # set self.image to new_image
        self.photo = new_image
        # save
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title
 
 
class AdvisorMsg (models.Model):
    AdvisorName = models.CharField(max_length=200, blank = True)
    AdvisorDegi = models.CharField(max_length=200, blank = True)
    photo = models.ImageField(upload_to='ChairmanMsg/', blank = True)
    message = RichTextField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views=models.IntegerField(default=0)

    class Meta:
        verbose_name = 'Chairman Message'
        verbose_name_plural = 'Chairman Message'

    #for compress images
    if photo.blank == False :
        def save(self, *args, **kwargs):

            # call the compress function
            new_image = compress(self.photo)
            # set self.image to new_image
            self.photo = new_image
            # save
            super().save(*args, **kwargs)
    def __str__(self):
        return self.AdvisorName
    
class CollaborationSlider (models.Model):
    title = models.CharField(max_length=200, blank = True)
    photo = models.ImageField(upload_to='CollaborationSlider/', blank = False)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)

       #for compress images
    def save(self, *args, **kwargs):
       # call the compress function
        new_image = compress(self.photo)
        # set self.image to new_image
        self.photo = new_image
        # save
        super().save(*args, **kwargs)
    def __str__(self):
        return self.title

class LetestNews(models.Model):
    title = models.CharField(max_length=200, blank = True)
    pdf = models.FileField(upload_to='LetestNews/pdf/', blank = True)
    photo = models.ImageField(upload_to='LetestNews/photo/', blank = True)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(blank = False, verbose_name ='On Date')
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views=models.IntegerField(default=0)
    
    #for compress images
    if photo.blank == False :
        def save(self, *args, **kwargs):

            # call the compress function
            new_image = compress(self.photo)
            # set self.image to new_image
            self.photo = new_image
            # save
            super().save(*args, **kwargs)
            
    def __str__(self):
        return self.title  


class People(models.Model):
    name = models.TextField(max_length=40,null=True,blank=True)
    designation = models.TextField(max_length=100,null=True,blank=True)
    university = models.TextField(max_length=300,null=True,blank=True)
    category = models.CharField(max_length=30,choices=PEOPLE_CHOICES,default="research_student")
    img = models.FileField(upload_to="people/")
    status = models.IntegerField(choices=STATUS, default = 1)


    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name = "People"
    
class PublicationCategory(models.Model):
    PublicationType = models.CharField(max_length= 20, blank = True , default="")
    class Meta:
        verbose_name = ("Publication Type")
        verbose_name_plural = ("Publication Types")
          
    def __str__(self):
        return self.status
    
class Publications(models.Model):
    
    Publication_Title = models.CharField(max_length=200, blank = False, default="")
    Author = models.ManyToManyField(People, default="")
    abstract =  RichTextField(blank=True, null=True , default = "")
    PublicationCategory = models.ForeignKey(PublicationCategory, verbose_name=("Publication Type"), on_delete=models.CASCADE , default="")
    DOI = models.CharField(max_length=200, blank = False, default="")
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views = models.IntegerField(default=0)
      

    class Meta:
        verbose_name = ("Publications")
        verbose_name_plural = ("Publications")


    def __str__(self):
        return self.project_Title
    # def get_absolute_url(self):
    #     return reverse('CapstoneProject:capstoneProject_detail', args=[self.slug])

class ProjectCategory(models.Model):
    ProjectType = models.CharField(max_length= 20, blank = True , default="")
    class Meta:
        verbose_name = ("Projcet Type")
        verbose_name_plural = ("Projcet Types")
          
    def __str__(self):
        return self.status
    

class Project(models.Model):
    
    project_Title = models.CharField(max_length=200, blank = False, default="")
    Author = models.ManyToManyField(People, default="")
    abstract =  RichTextField(blank=True, null=True , default = "")
    ProjectCategory = models.ForeignKey(ProjectCategory, verbose_name=("Projcet Type"), on_delete=models.CASCADE , default="")
    Github_Link = models.CharField(max_length=200, blank = False, default="")
    Funding_agency= models.CharField(max_length=200, blank = False, default="")
    Funding_period = models.CharField(max_length=200, blank = False, default="")
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views = models.IntegerField(default=0)
      

    class Meta:
        verbose_name = ("Project")
        verbose_name_plural = ("Project")


    def __str__(self):
        return self.project_Title
    # def get_absolute_url(self):
    #     return reverse('CapstoneProject:capstoneProject_detail', args=[self.slug])
