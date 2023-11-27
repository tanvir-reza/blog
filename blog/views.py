from django.shortcuts import render
from django.views import generic
from django.db.models import Q

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
from users.models import ResearchAreaPeople


def index(request):
    about = About.objects.first()
    l_news = LetestNews.objects.first()
    l_resaearch = Publications.objects.first()
    l_project = Project.objects.first()
    founders = People.objects.filter(
        category="Founder & Research Director")[:1]
    collabs = CollaborationSlider.objects.all()
    sliders_count = HomeSlider.objects.count()
    print(sliders_count)
    sliders = HomeSlider.objects.all()
    context = {"sliders": sliders, "l_news": l_news, "collabs": collabs, "sliders_count": sliders_count,
               "about": about, "l_project": l_project, "founders": founders, "l_resaearch": l_resaearch}
    return render(request, "index.html", context)


def founderMsg(request):
    post = Founder.objects.first()
    context = {"post": post}
    return render(request, 'f-msg.html', context)


def people(request):
    founders = People.objects.filter(category="Founder & Research Director")
    advisor = People.objects.filter(category="Advisor")
    head = People.objects.filter(
        category="Head of the Department")
    lead = People.objects.filter(category="Lead Researcher")
    researcher = People.objects.filter(category="Researcher")
    research_ass = People.objects.filter(category="Research Assistant")
    research_int = People.objects.filter(category="Research Intern")

    alumnis = People.objects.filter(category="Alumni")

    print(advisor)

    print(founders)

    context = {"advisors": advisor, "founders": founders, "alumnis": alumnis,
               "heads": head, "lead": lead, "researchers": researcher, "research_ass": research_ass,"research_int":research_int}
    return render(request, 'people.html', context)
# def people(request):
#     return render(request,"people.html")


def peopleDetailsView(request, slug):
    post = People.objects.get(slug=slug)
    post.total_views = post.total_views+1
    post.save()
    return render(request, 'people_details.html', {'post': post})


def about(request):
    post = About.objects.first()
    context = {"post": post}
    return render(request, "about.html", context)


def publications(request):

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

    context = {"Authored_books": Authored_books, "Edited_Volumes": Edited_Volumes, "Journal_Papers": Journal_Papers,
               "Book_Chapters": Book_Chapters, "Conference_Proceedings": Conference_Proceedings, "Conference_Papers": Conference_Papers}

    return render(request, 'publications.html', context)


def projects(request):

    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects.html", context)


def ResearchUnit(request):
    return render(request, "research_unit.html")


def OpenPositions(request):
    data = openPositon.objects.all()
    data2 = ResearchTopic.objects.all()
    print(data)
    context = {"data": data, "data2": data2}
    return render(request, "openposition.html", context)


def TrainingProgram(request):
    post = trainingProgram.objects.first()
    context = {"post": post}
    return render(request, "traning.html", context)


def Contact(request):

    return render(request, "contact.html")


# eight research fields page connection start
def DAIBI(request):
    d = "Department of Artificial Intelligence and Biomedical Imaging"
    s = "DAIBI"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')
    

    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        
        'd': d, 's': s, 'topic': topic
    }

    return render(request, 'DAIBI.html', context)


def DDLNCV(request):
    d = "Department of Deep Learning and Computer Vision"
    s = "DDLNCV"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')

    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        
        'd': d, 's': s, 'topic': topic
    }
    return render(request, 'DAIBI.html', context)


def DNLPT(request):
    d = "Department of Natural Language Processing and Transformers"
    s = "DNLPT"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')


    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        'd': d, 's': s, 'topic': topic
    }

    return render(request, 'DAIBI.html', context)


def DIOTR(request):
    d = "Department of Internet of Things and Robotics"
    s = "DIOTR"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')

    

    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        
        'd': d, 's': s, 'topic': topic
    }

    return render(request, 'DAIBI.html', context)


def DAISH(request):
    d = "Department of Artificial Intelligence in Security and Healthcare"
    s = "DAISH"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')
    

    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        
        'd': d, 's': s, 'topic': topic
    }

    return render(request, 'DAIBI.html', context)


def DDSFL(request):
    d = "Department of Data Science and Federated Learning"
    s = "DDSFL"
    topic = ResearchTopic.objects.filter(slug=s).values('short_bio').first()
    heads = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Head of the Department')
    lead_researchers = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Lead Researcher')
    researcher = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Researcher')
    research_assistants = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Assistant')
    research_interns = ResearchAreaPeople.objects.filter(
        research_topic__research_topic=d, designation__title='Research Intern')
    

    context = {
        "heads": heads, "lead_researchers": lead_researchers,
        "researcher": researcher, "research_assistants": research_assistants, "research_interns": research_interns,
        
        'd': d, 's': s, 'topic': topic
    }

    return render(request, 'DAIBI.html', context)


# def re_cv(request):
#     topic = People.objects.filter(research_Topic__slug='CV')
#     data = ResearchTopic.objects.filter(slug='CV').first()
#     return render(request, 're_cv.html', {'CV': topic, 'data': data})


# def re_others(request):
#     topic = People.objects.filter(research_Topic__slug='RL')
#     data = ResearchTopic.objects.filter(slug='RL').first()
#     return render(request, 're_others.html', {'RL': topic, 'data': data})
# # eight research fields page connection end
