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


def index(request):
    info = Blog.objects.first()
    about = About.objects.first()
    l_news = LetestNews.objects.first()
    # l_resaearch = LetestNews.objects.all().order_by("")
    l_project = Project.objects.all().order_by("-created_on")[1]
    founders = People.objects.filter(
        category="founder_&_research_directors")[:2]
    collabs = CollaborationSlider.objects.all()
    sliders_count = HomeSlider.objects.count()
    print(sliders_count)
    sliders = HomeSlider.objects.all()
    context = {"info": info, "sliders": sliders, "l_news": l_news, "collabs": collabs,
               "sliders_count": sliders_count, "about": about, "l_project": l_project, "founders": founders}
    return render(request, "index.html", context)


def people(request):
    info = Blog.objects.first()
    advisor = People.objects.filter(category="advisor")
    ra = People.objects.filter(category="research_assistant")
    rs = People.objects.filter(category="research_student")
    founders = People.objects.filter(category="founder_&_research_directors")
    coordinators = People.objects.filter(
        category="research_coordinator_&_lead_research_assistant")
    alumnis = People.objects.filter(category="alumni")

    context = {"advisors": advisor, "research_assistants": ra, "research_students": rs,
               "info": info, "founders": founders, "coordinators": coordinators, "alumnis": alumnis}
    return render(request, 'people.html', context)
# def people(request):
#     return render(request,"people.html")


def peopleDetailsView(request, post_id):
    post = People.objects.get(pk=post_id)
    post.total_views = post.total_views+1
    post.save()
    return render(request, 'People_details.html', {'post': post})


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
    return render(request, "openposition.html")


def TrainingProgram(request):
    return render(request, "traning.html")


def Contact(request):
    info = Blog.objects.first()
    context = {"info": info}

    return render(request, "contact.html", context)
