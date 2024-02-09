from django.shortcuts import render
from django.conf import settings
from django.views import generic
from django.db.models import Q
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
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
from users.models import VisionAMIRL
from users.models import MissionAMIRL
from users.models import *
from .forms import ApplicantForm
from django.contrib import messages  # Import the messages module

def index(request):
    about = About.objects.first()
    l_news = LetestNews.objects.first()
    l_resaearch = Publications.objects.first()
    l_project = Project.objects.first()
    founders = People.objects.filter(
        category__CategoryName="Founder & Research Director")[:1]
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
    founders = People.objects.filter(category__CategoryName="Founder & Research Director")
    advisor = People.objects.filter(category__CategoryName="Advisor")
    head = People.objects.filter(
        category__CategoryName="Head of the Department")
    lead = People.objects.filter(category__CategoryName="Lead Researcher")
    researcher = People.objects.filter(category__CategoryName="Researcher")
    research_ass = People.objects.filter(category__CategoryName="Research Assistant")
    research_int = People.objects.filter(category__CategoryName="Research Intern")
    alumnis = People.objects.filter(category__CategoryName="Alumni")

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


# def publications(request):
#     post=Publications.objects.all()
#     Authored_books = Publications.objects.filter(
#         category__PublicationType='Authored Books')
#     # when you want to show data from another table you have to use first tablecoloumn then __ then second table coloumn ex here we want to show data from publication table and publicationcategory table so we have to use category__PublicationType
#     # [0:10] this will show only 10 data from the query set
#     # print(Authored_books) #this will print the query set
#     Edited_Volumes = Publications.objects.filter(
#         category__PublicationType='Edited Volumes')
#     Journal_Papers = Publications.objects.filter(
#         category__PublicationType='Journal Papers')
#     Book_Chapters = Publications.objects.filter(
#         category__PublicationType='Book Chapters')
#     Conference_Proceedings = Publications.objects.filter(
#         category__PublicationType='Conference Proceedings')
#     Conference_Papers = Publications.objects.filter(
#         category__PublicationType='Conference Papers')

#     context = {"post":post.order_by('-publish_on'),"Authored_books": Authored_books, "Edited_Volumes": Edited_Volumes, "Journal_Papers": Journal_Papers,
#                "Book_Chapters": Book_Chapters, "Conference_Proceedings": Conference_Proceedings, "Conference_Papers": Conference_Papers}

#     return render(request, 'publications.html', context)

def publications(request):
    publications_dict = {}

    # Fetch all publications and organize them by year
    all_publications = Publications.objects.all().order_by('-publish_on')

    for publication in all_publications:
        year = publication.publish_on.year
        if year not in publications_dict:
            publications_dict[year] = {'Journal Papers': [], 'Book Chapters': [], 'Conference Papers': []}

        # Organize publications by category
        if publication.category.PublicationType == 'Journal Papers':
            print()
            publications_dict[year]['Journal Papers'].append(publication)
        elif publication.category.PublicationType == 'Book Chapters':
            publications_dict[year]['Book Chapters'].append(publication)
        elif publication.category.PublicationType == 'Conference Papers':
            publications_dict[year]['Conference Papers'].append(publication)
         # Print data for debugging
        #print(f"Year: {year}, Category: {publication.category.PublicationType}, Publication Title: {publication.Publication_Title},{publication.details}")

    context = {"publications_dict": publications_dict}
    return render(request, 'publications.html', context)

def projects(request):

    projects = Project.objects.all()
    context = {"projects": projects}
    return render(request, "projects.html", context)


def ResearchUnit(request):   
    return render(request, "research_unit.html")

def Vision(request):
    Vision = VisionAMIRL.objects.all()
    context = {"Vision": Vision}
    return render(request, "vision.html", context)
def Achivement(request):
    Achivement = Achivements.objects.all()
    context = {"Achivement": Achivement}
    return render(request, "achivement.html",context)

def Mison(request):
    Mission = MissionAMIRL.objects.all()
    context = {"Mission": Mission}
    return render(request, "mission.html",context)

def WhyAMIRL(request):
    Why = WhyatAMIRL.objects.all()
    context = {"Why": Why}
    return render(request, "why.html",context)

def OpenPositions(request):
    data = openPositon.objects.all()
    data2 = "Welcome to the Comprehensive Guide for Research Lab Positions. This page outlines the diverse opportunities available within our esteemed research lab, ranging from leadership roles to internships. As we navigate through the requirements for each position, we also acknowledge the potential for flexibility, especially for individuals with international degrees"

    if request.method == 'POST':
        form = ApplicantForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Applicant.objects.filter(email=email).exists():
                messages.error(request, 'You have already applied with this email.')
            else:
                applicant = form.save()
                send_confirmation_email(email)
                messages.success(request, 'Your application has been submitted successfully! Check your email for confirmation.Check your email for a confirmation message. If you do not see the email, check other places it might be, like your junk, spam, social, or other folders.')

    else:
        form = ApplicantForm()

    context = {"data": data, "data2": data2, 'form': form}
    return render(request, "openposition.html", context)
def send_confirmation_email(email):
    subject = 'Application Confirmation - AMIR Lab'
    
    # Assuming you have an email template named 'confirmation_email.html'
    html_message = render_to_string('confirmation_email.html')
    plain_message = strip_tags(html_message)
    
    # Read email configuration from settings
    from_email = settings.EMAIL_HOST_USER  # Use the configured email address as the sender
    to_email = [email]

    # Create an EmailMultiAlternatives object
    msg = EmailMultiAlternatives(subject, plain_message, from_email, to_email)
    
    # Attach the HTML content
    msg.attach_alternative(html_message, "text/html")

    # Attach images with Content-ID
    # msg.attach_file('blog\static\images\social_logo\facebook-logo.png', 'image/png')
    # msg.attach_file('blog/static/images/social_logo/linkedin-logo.png', 'image/png')
    # msg.attach_file('blog/static/images/social_logo/twitter-logo.png', 'image/png')

    # Send the email
    msg.send()


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
    d = "Department of Natural Language Processing and Computational Linguistics"
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
    d = "Department of Internet of Things and Block Chain"
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
def AdministUnit(request):
    CE=AdminCommitteeDetails.objects.filter(
        Committee__title='Chief Executive')
    Web = AdminCommitteeDetails.objects.filter(
        Committee__title='Web Administration')
    Design = AdminCommitteeDetails.objects.filter(
        Committee__title='Design and Content Creation')
    Social = AdminCommitteeDetails.objects.filter(
        Committee__title='Social Media Administration')
    HR = AdminCommitteeDetails.objects.filter(
        Committee__title='International Relations and HR')

    context = {
        "CE":CE,
        "Web": Web,
        "Design":Design,
        "Social":Social,
        "HR":HR
    }

    return render(request, 'administunit.html', context)

def ApprovalCommittee(request):
    heads = AdminCommitteeDetails.objects.filter(
        Committee__title='Research Ethics Approval Committee')

    context = {
        "heads": heads
    }

    return render(request, 'approvalcommittee.html', context)


