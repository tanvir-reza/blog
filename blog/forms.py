# forms.py
from django import forms
from users.models import Applicant
from users.models import ResearchTopic

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'CurrentAffiliations', 'email','Phone','InterestedResearchTeam','Position','PreviousExperience','resume']
def __init__(self, *args, **kwargs):
        super(ApplicantForm, self).__init__(*args, **kwargs)
        self.fields['InterestedResearchTeam'].queryset = ResearchTopic.objects.all()