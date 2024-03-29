from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views
from rest_framework import routers
from django.urls import path,include,re_path
from django.views.static import serve


from website import restApiViews
router = routers.DefaultRouter()
router.register(r'peoples', restApiViews.PeopleViewSet)
router.register(r'designations', restApiViews.PeopleDesignationViewSet)
router.register(r'researchtopic', restApiViews.Research_TopicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('people/', views.people, name="people"),
    path('about/', views.about, name="about"),
    path('publications/', views.publications, name="publications"),
    path('projects/', views.projects, name="projects"),
    path('research-unit/', views.ResearchUnit, name="ResearchUint"),
    path('Open-Positions/', views.OpenPositions, name="OpenPositions"),
    path('Founder-Message/', views.founderMsg, name="founderMsg"),
    path('Training-Program/', views.TrainingProgram, name="TrainingProgram"),
    path('Contact/', views.Contact, name="Contact"),
    # path('people/',views.people,name="people"),
    path('DAIBI/', views.DAIBI, name='DAIBI'),
    path('DDLNCV/', views.DDLNCV, name='DDLNCV'),
    path('DNLPT/', views.DNLPT, name='DNLPT'),
    path('DIOTR/', views.DIOTR, name='DIOTR'),
    path('DAISH/', views.DAISH, name='DAISH'),
    path('DDSFL/', views.DDSFL, name='DDSFL'),
    path('Vision/', views.Vision, name='Vision'),
    path('Mison/', views.Mison, name='Mison'),
    path('Achivement/', views.Achivement, name='Achivement'),
    path('WhyAMIRL/', views.WhyAMIRL, name='WhyAMIRL'),
    path('founderMsg/', views.founderMsg, name='founderMsg'),
    path('ApprovalCommittee/', views.ApprovalCommittee, name='ApprovalCommittee'),
    path('AdministUnit/', views.AdministUnit, name='AdministUnit'),
    

    # path('CV', views.re_cv, name='re_cv'),
    # path('RL', views.re_others, name='re_others'),
    path('peopleDetailsView/<slug>/', views.peopleDetailsView, name='peopleDetailsView'),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'website.views.custom_404'
