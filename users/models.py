from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from PIL import Image
from io import BytesIO
import uuid
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
 
 
# class AdvisorMsg (models.Model):
#     AdvisorName = models.CharField(max_length=200, blank = True)
#     AdvisorDegi = models.CharField(max_length=200, blank = True)
#     photo = models.ImageField(upload_to='ChairmanMsg/', blank = True)
#     message = RichTextField(blank=True, null=True)
#     updated_on = models.DateTimeField(auto_now = True)
#     created_on = models.DateTimeField(auto_now_add =True)
#     status = models.IntegerField(choices=STATUS, default = 1)
#     total_views=models.IntegerField(default=0)

#     class Meta:
#         verbose_name = 'Chairman Message'
#         verbose_name_plural = 'Chairman Message'

#     #for compress images
#     if photo.blank == False :
#         def save(self, *args, **kwargs):

#             # call the compress function
#             new_image = compress(self.photo)
#             # set self.image to new_image
#             self.photo = new_image
#             # save
#             super().save(*args, **kwargs)
#     def __str__(self):
#         return self.AdvisorName
    
# class CollaborationSlider (models.Model):
#     title = models.CharField(max_length=200, blank = True)
#     photo = models.ImageField(upload_to='CollaborationSlider/', blank = False)
#     updated_on = models.DateTimeField(auto_now = True)
#     created_on = models.DateTimeField(auto_now_add =True)
#     status = models.IntegerField(choices=STATUS, default = 1)

#        #for compress images
#     def save(self, *args, **kwargs):
#        # call the compress function
#         new_image = compress(self.photo)
#         # set self.image to new_image
#         self.photo = new_image
#         # save
#         super().save(*args, **kwargs)
#     def __str__(self):
#         return self.title

# class LetestNews(models.Model):
#     title = models.CharField(max_length=200, blank = True)
#     pdf = models.FileField(upload_to='LetestNews/pdf/', blank = True)
#     photo = models.ImageField(upload_to='LetestNews/photo/', blank = True)
#     updated_on = models.DateTimeField(auto_now = True)
#     created_on = models.DateTimeField(blank = False, verbose_name ='On Date')
#     status = models.IntegerField(choices=STATUS, default = 1)
#     total_views=models.IntegerField(default=0)
    
#     #for compress images
#     if photo.blank == False :
#         def save(self, *args, **kwargs):

#             # call the compress function
#             new_image = compress(self.photo)
#             # set self.image to new_image
#             self.photo = new_image
#             # save
#             super().save(*args, **kwargs)
            
#     def __str__(self):
#         return self.title  
class Designation(models.Model):
    title = models.CharField(max_length=250, unique=True, default="")
    dsgOrder = models.CharField(max_length=3, blank=False, default="", unique=True)
    slug = models.SlugField(default="", unique=True)


    class Meta:
        ordering = ["-dsgOrder"]
        verbose_name = 'Faculty designation'
        verbose_name_plural = 'Faculty designations'

    def __str__(self):
        return self.title

    # def get_absoulte_url(self):
    #     return reverse('desginations:list_by_desginations', args=[self.slug])
    
class ResearchTopic(models.Model):
    research_topic = models.CharField(max_length=100)
    slug = models.CharField(max_length=250)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views=models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Research Topics'

    def __str__(self):
        return self.research_topic

class People(models.Model):
    FullName = models.CharField(max_length=200, blank = False, verbose_name = ("Full Name"), null=True)
    BanglaName = models.CharField(max_length=200, blank = True)
    designation = models.ForeignKey(Designation, on_delete= models.CASCADE, verbose_name ="Designation", blank = False , null=True)  
    LoginUser = models.ForeignKey(User, on_delete= models.CASCADE, verbose_name = ("Select your E-mail"),null=True )
    university = models.TextField(max_length=300,null=True,blank=True)
    category = models.CharField(max_length=30,choices=PEOPLE_CHOICES,default="research_student")
    img = models.FileField(upload_to="people/")
    email= models.CharField(max_length=200, blank = True)
    office_Phone = models.CharField(max_length=200, blank = True)
    teachingArea = models.CharField(max_length=200, blank = True, verbose_name = ("Teaching Area"))
    research_Topic = models.ManyToManyField(ResearchTopic, blank=True, null=True , default="")
    google_ScholarLink = models.CharField(max_length=200, blank = True)
    research_Gate_Link = models.CharField(max_length=200, blank = True)
    website = models.CharField(max_length=200, blank = True)
    other_Contact = models.CharField(max_length=200, blank = True)
    office_RoomNo = models.CharField(max_length=20, blank = True)
    officeBuilding = models.CharField(max_length=30, blank = True)
    academic_Background = RichTextField(blank=True, null=True)
    biography = RichTextField(blank=True, null=True)
    leav_status = models.CharField(max_length=200, blank = True, verbose_name = ("Leave status(any if)"))
    teachingExprience = RichTextField(blank=True, null=True)
    Professional_Certifications = RichTextField(blank=True, null=True)
    researchArea = RichTextField(blank=True, null=True)
    research_Interest =  RichTextField(blank=True, null=True)
    selected_Publications = RichTextField(blank=True, null=True, verbose_name ="Book_Chapter")
    award = RichTextField(blank=True, null=True)
    researchGrant  = RichTextField(blank=True, null=True)
    journal_Papers = RichTextField(blank=True, null=True)
    conference_Papers = RichTextField(blank=True, null=True)
    professional_membership= RichTextField(blank=True, null=True)
    professional_international_work = RichTextField(blank=True, null=True)
    # f_photo = models.ImageField(upload_to='PeopleImagesGallary/', blank = True, verbose_name = ("FacultyPhotoGalary"))
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views=models.IntegerField(default=0)

    def __str__(self):
        return self.FullName
    
    
    class Meta:
         verbose_name = "People"
    
class PublicationCategory(models.Model):
    PublicationType = models.CharField(max_length= 20, blank = True , default="")
    class Meta:
        verbose_name = ("Publication Type")
        verbose_name_plural = ("Publication Types")
          
    def __str__(self):
        return self.PublicationType
    
class Publications(models.Model):
    Publication_Title = models.CharField(max_length=200, blank = False, default="")
    Author = models.ManyToManyField(People, default="")
    abstract =  RichTextField(blank=True, null=True , default = "")
    category = models.ForeignKey(PublicationCategory, verbose_name=("PublicationCategory"), on_delete=models.CASCADE , default="")
    DOI = models.CharField(max_length=200, blank = False, default="")
    status = models.IntegerField(choices=STATUS, default = 1)
    total_views = models.IntegerField(default=0)
      

    class Meta:
        verbose_name = ("Publications")
        verbose_name_plural = ("Publications")


    def __str__(self):
        return self.Publication_Title
    # def get_absolute_url(self):
    #     return reverse('CapstoneProject:capstoneProject_detail', args=[self.slug])

class ProjectCategory(models.Model):
    ProjectType = models.CharField(max_length= 20, blank = True , default="")
    class Meta:
        verbose_name = ("Projcet Type")
        verbose_name_plural = ("Projcet Types")
          
    def __str__(self):
        return self.ProjectType
    

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
