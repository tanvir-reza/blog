from django.contrib.auth.models import User, Group
from rest_framework import serializers
from users.models import *
from website.models import *


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicFieldsModelSerializer, self).__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class DesignationSerializer(DynamicFieldsModelSerializer):
        class Meta:
            model = Designation
            fields = '__all__'


class Research_TopicSerializer(DynamicFieldsModelSerializer):
        class Meta:
            model = ResearchTopic
            fields = '__all__'

class PeopleSerializer(DynamicFieldsModelSerializer):


        class Meta:
            model = People
            fields = '__all__'