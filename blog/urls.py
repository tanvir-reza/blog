from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views
from rest_framework import routers

from website import restApiViews
router = routers.DefaultRouter()
router.register(r'peoples', restApiViews.PeopleViewSet)
router.register(r'designations', restApiViews.PeopleDesignationViewSet)
router.register(r'researchtopic', restApiViews.Research_TopicViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('people', views.people, name="people"),
    path('publications', views.publications, name="publications"),
    path('projects', views.projects, name="projects"),
    path('research-unit/', views.ResearchUnit, name="ResearchUint"),
    path('Open-Positions', views.OpenPositions, name="OpenPositions"),
    path('Training-Program', views.TrainingProgram, name="TrainingProgram"),
    path('Contact', views.Contact, name="Contact"),
    # path('people/',views.people,name="people"),
    path('CML', views.re_cml, name='re_cml'),
    path('QML', views.re_qml, name='re_qml'),
    path('NLP', views.re_nlp, name='re_nlp'),
    path('RNN', views.re_rnn, name='re_rnn'),
    path('XAI', views.re_xai, name='re_xai'),
    path('MU', views.re_mu, name='re_mu'),
    path('CV', views.re_cv, name='re_cv'),
    path('ROF', views.re_others, name='re_others'),
    path('peopleDetailsView/<post_id>/', views.peopleDetailsView, name='peopleDetailsView'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
