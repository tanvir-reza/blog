from django.shortcuts import render
from django.views.generic import ListView

from website.models import Blog
from users.models import People
from users.models import HomeSlider
from users.models import Publications


def index(request):
    info = Blog.objects.first()
    sliders_count = HomeSlider.objects.count()
    print(sliders_count)
    sliders = HomeSlider.objects.all()
    context = {"info":info,"sliders":sliders}
    return render(request,"index.html",context)



def people(request):
    info = Blog.objects.first()
    advisor = People.objects.filter(category = "advisor")
    ra = People.objects.filter(category = "research_assistant")
    rs = People.objects.filter(category = "research_student")

    context  = {"advisors" : advisor, "research_assistants": ra,"research_students": rs,"info":info}
    return render(request,'people.html',context)
# def people(request):
#     return render(request,"people.html")
def publications(request):
    info = Blog.objects.first()
    Authored_books = Publications.objects.filter(category__PublicationType = 'Authored Books')[:10] #when you want to show data from another table you have to use first tablecoloumn then __ then second table coloumn ex here we want to show data from publication table and publicationcategory table so we have to use category__PublicationType
    #print(Authored_books)
    
    context  = {"info":info,"Authored_books":Authored_books}
    return render(request,'publications.html',context)
def projects(request):
    return render(request,"projects.html")
def FocusAreas(request):
    return render(request,"focus.html")
def OpenPositions(request):
    return render(request,"openposition.html")
def TrainingProgram(request):
    return render(request,"traning.html")
def Contact(request):
    return render(request,"contact.html")
