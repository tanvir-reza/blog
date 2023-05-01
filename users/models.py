from django.db import models
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
PEOPLE_CHOICES = (
    ('advisor','Advisor'),
    ('research_assistant', 'Research Assistant'),
    ('research_student','Research Student'),
)

class HomeSlider (models.Model):
    title = models.CharField(max_length=200, blank = True)
    slogan = models.CharField(max_length=200, blank = True)
    Details = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='HomeSlider/', blank = False)
    updated_on = models.DateTimeField(auto_now = True)
    created_on = models.DateTimeField(auto_now_add =True)
    status = models.IntegerField(choices=STATUS, default = 1)

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
    

