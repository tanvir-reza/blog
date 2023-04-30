from django.shortcuts import render
from django.views.generic import ListView

from website.models import Blog
from users.models import People


def index(request):
    info = Blog.objects.first()
    context = {"info":info}
    return render(request,"index.html",context)



# def people(request):
#     advisor = People.objects.filter(category = "advisor")
#     ra = People.objects.filter(category = "research_assistant")
#     rs = People.objects.filter(category = "research_student")

#     context  = {"advisors" : advisor, "research_assistants": ra,"research_students": rs}
#     return render(request,'people.html',context)
def people(request):
    return render(request,"people.html")
def publications(request):
    return render(request,"publications.html")
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
