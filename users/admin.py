from django.contrib import admin
from . import models
from django.conf import settings
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.db import transaction

# Register your models here.
from .models import People
admin.site.site_header = "AMIRL ADMIN"
admin.site.site_title = "@AMIRL"
admin.site.index_title = "API List"

admin.site.register(models.Publications)
admin.site.register(models.PublicationCategory)
admin.site.register(models.HomeSlider)
admin.site.register(models.Designation)
admin.site.register(models.ResearchTopic)
admin.site.register(models.Project)
admin.site.register(models.ProjectCategory)
admin.site.register(models.LetestNews)
admin.site.register(models.CollaborationSlider)
admin.site.register(models.About)
admin.site.register(models.openPositon)
admin.site.register(models.openPositonCategory)
admin.site.register(models.Founder)
admin.site.register(models.trainingProgram)
admin.site.register(models.ResurachUnit_Designation)
admin.site.register(models.ResearchAreaPeople)
admin.site.register(models.PeopleCategory)
admin.site.register(models.VisionAMIRL)
admin.site.register(models.MissionAMIRL)
admin.site.register(models.WhyatAMIRL)
admin.site.register(models.Achivements)
admin.site.register(models.AdminCommittee)
admin.site.register(models.AdminCommitteeDetails)
def send_confirmation_email(modeladmin, request, queryset):
    # print(f"ModelAdmin: {modeladmin}")
    # print(f"Request: {request}")

    # Your custom action logic here
    # print("Sending confirmation email...")

    for applicant in queryset:
        if not applicant.confirmation_email_sent:
            send_confirmation_email_to_applicant(applicant)

    # print("Confirmation email sent.")

send_confirmation_email.short_description = "Send confirmation email to selected applicants"

# def send_confirmation_email(modeladmin, request, queryset):
#     for applicant in queryset:
#         if not applicant.confirmation_email_sent:
#             send_confirmation_email_to_applicant(applicant)

# send_confirmation_email.short_description = "Send confirmation email to selected applicants"

def send_confirmation_email_to_applicant(applicant):
    try:
        subject = 'Application Confirmation - AMIR Lab'
        html_message = render_to_string('acceptance_email.html', {'applicant': applicant})
        plain_message = strip_tags(html_message)
        from_email = settings.EMAIL_HOST_USER  # Replace with your email
        to_email = [applicant.email]

        print(f"Sending email to: {to_email}")

        msg = EmailMultiAlternatives(subject, plain_message, from_email, to_email)
        msg.attach_alternative(html_message, "text/html")

        # print("Email content:")
        # print(f"Subject: {subject}")
        # print(f"From: {from_email}")
        # print(f"To: {to_email}")

        msg.send()
        # print("Email sent successfully!")
        # Update confirmation_email_sent to True
        with transaction.atomic():
            applicant.confirmation_email_sent = True
            applicant.save()
    except Exception as e:
        print(f"Error sending email: {str(e)}")

class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'accepted', 'confirmation_email_sent')
    actions = [send_confirmation_email]
    print(actions)
admin.site.register(models.Applicant, ApplicantAdmin)
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['FullName', 'designation', 'university', 'email']  # Add other fields as needed
    search_fields = ['FullName', 'LoginUser__username', 'LoginUser__email']  # Search fields based on user and people attributes

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(LoginUser=request.user)

admin.site.register(People, PeopleAdmin)