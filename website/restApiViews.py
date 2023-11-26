from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import *
from users.models import *
from website.models import *


class PeopleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = People.objects.all()
    serializer_class = PeopleSerializer

class PeopleDesignationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Designation.objects.all()
    serializer_class = DesignationSerializer

class Research_TopicViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ResearchTopic.objects.all()
    serializer_class = Research_TopicSerializer
   