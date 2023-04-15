from django.db import models


PEOPLE_CHOICES = (
    ('advisor','Advisor'),
    ('research_assistant', 'Research Assistant'),
    ('research_student','Research Student'),
)

class People(models.Model):
    name = models.TextField(max_length=40,null=True,blank=True)
    designation = models.TextField(max_length=100,null=True,blank=True)
    university = models.TextField(max_length=300,null=True,blank=True)
    category = models.CharField(max_length=30,choices=PEOPLE_CHOICES,default="research_student")
    img = models.FileField(upload_to="people/")


    def __str__(self):
        return self.name
    
    class Meta:
         verbose_name = "People"
    

