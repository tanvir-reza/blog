from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('people', views.people, name="people"),
    path('publications', views.publications, name="publications"),
    path('projects', views.projects, name="projects"),
    path('Focus-Areas', views.FocusAreas, name="FocusAreas"),
    path('Open-Positions', views.OpenPositions, name="OpenPositions"),
    path('Training-Program', views.TrainingProgram, name="TrainingProgram"),
    path('Contact', views.Contact, name="Contact"),
    # path('people/',views.people,name="people"),
    path('peopleDetailsView/<post_id>/', views.peopleDetailsView, name='peopleDetailsView'),
]


urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
