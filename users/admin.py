from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header = "AMIRL ADMIN"
admin.site.site_title = "@MIRL"
admin.site.index_title = "API List"

admin.site.register(models.People)
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