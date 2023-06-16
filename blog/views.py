from django.shortcuts import render
from django.views import generic

from website.models import Blog
from users.models import People
from users.models import HomeSlider
from users.models import Publications
from users.models import Project
from users.models import LetestNews
from users.models import CollaborationSlider
from users.models import About
from users.models import Founder
from users.models import openPositon
from users.models import trainingProgram
from users.models import ResearchTopic



def index(request):
    info = Blog.objects.first()
    about = About.objects.first()
    l_news = LetestNews.objects.first()
    l_resaearch = Publications.objects.first()
    l_project = Project.objects.first()
    founders = People.objects.filter(
        category="Founder & Research Director")[:2]
    collabs = CollaborationSlider.objects.all()
    sliders_count = HomeSlider.objects.count()
    print(sliders_count)
    sliders = HomeSlider.objects.all()
    context = {"info": info, "sliders": sliders, "l_news": l_news, "collabs": collabs, "sliders_count": sliders_count, "about": about, "l_project": l_project, "founders": founders , "l_resaearch":l_resaearch}
    return render(request, "index.html", context)


def founderMsg(request):
    post = Founder.objects.first()
    context = {"post": post}
    return render(request,'f-msg.html',context)


def people(request):
    info = Blog.objects.first()
    advisor = People.objects.filter(category="Advisor")
    researchAssociates = People.objects.filter(category="Research Associates")
    ra = People.objects.filter(category="Research Assistants")
    rs = People.objects.filter(category="Research Intern Student")
    founders = People.objects.filter(category="Founder & Research Director")
    coordinators = People.objects.filter(
        category="Research Coordinator & Lead R.A")
    alumnis = People.objects.filter(category="Alumni")

    context = {"advisors": advisor, "research_assistants": ra, "research_students": rs,
               "info": info, "founders": founders, "coordinators": coordinators, "alumnis": alumnis, "researchAssociates": researchAssociates}
    return render(request, 'people.html', context)
# def people(request):
#     return render(request,"people.html")


def peopleDetailsView(request, post_id):
    post = People.objects.get(pk=post_id)
    post.total_views = post.total_views+1
    post.save()
    return render(request, 'people_details.html', {'post': post})

def about(request):
    post = About.objects.first()
    context = {"post": post}
    return render(request, "about.html", context)

def publications(request):
    info = Blog.objects.first()
    Authored_books = Publications.objects.filter(
        category__PublicationType='Authored Books')
    # when you want to show data from another table you have to use first tablecoloumn then __ then second table coloumn ex here we want to show data from publication table and publicationcategory table so we have to use category__PublicationType
    # [0:10] this will show only 10 data from the query set
    # print(Authored_books) #this will print the query set
    Edited_Volumes = Publications.objects.filter(
        category__PublicationType='Edited Volumes')
    Journal_Papers = Publications.objects.filter(
        category__PublicationType='Journal Papers')
    Book_Chapters = Publications.objects.filter(
        category__PublicationType='Book Chapters')
    Conference_Proceedings = Publications.objects.filter(
        category__PublicationType='Conference Proceedings')
    Conference_Papers = Publications.objects.filter(
        category__PublicationType='Conference Papers')

    context = {"info": info, "Authored_books": Authored_books, "Edited_Volumes": Edited_Volumes, "Journal_Papers": Journal_Papers,
               "Book_Chapters": Book_Chapters, "Conference_Proceedings": Conference_Proceedings, "Conference_Papers": Conference_Papers}

    return render(request, 'publications.html', context)


def projects(request):
    info = Blog.objects.first()
    projects = Project.objects.all()
    context = {"info": info, "projects": projects}
    return render(request, "projects.html", context)


def ResearchUnit(request):
    return render(request, "research_unit.html")


def OpenPositions(request):
    data = openPositon.objects.all()
    data2 = ResearchTopic.objects.all()
    print(data)
    context = {"data" : data,"data2":data2}
    return render(request, "openposition.html",context)


def TrainingProgram(request):
    post = trainingProgram.objects.first()
    context = {"post": post}
    return render(request, "traning.html", context)


def Contact(request):
    info = Blog.objects.first()
    context = {"info": info}

    return render(request, "contact.html", context)


# eight research fields page connection start
def re_cml(request):
    topic = People.objects.filter(research_Topic__slug ='CML')
    return render(request, 're_cml.html', {'CML': topic})

def re_qml(request):
    topic = People.objects.filter(research_Topic__slug = 'QML')
    return render(request, 're_qml.html',{'QML': topic})

def re_nlp(request):
    topic = People.objects.filter(research_Topic__slug = 'NLP')
    return render(request, 're_nlp.html',{'NLP': topic})

def re_rnn(request):
    topic = People.objects.filter(research_Topic__slug = 'RNN')
    return render(request, 're_rnn.html',{'RNN': topic})

def re_xai(request):
    topic = People.objects.filter(research_Topic__slug = 'XAI')
    return render(request, 're_xai.html',{'XAI': topic})

def re_mu(request):
    topic = People.objects.filter(research_Topic__slug = 'MU')
    return render(request, 're_mu.html',{'MU': topic})

def re_cv(request):
    topic = People.objects.filter(research_Topic__slug = 'CV')
    return render(request, 're_cv.html',{'CV': topic})

def re_others(request):
    topic = People.objects.filter(research_Topic__slug = 'ROF')
    return render(request, 're_others.html',{'ROF': topic})
# eight research fields page connection end
