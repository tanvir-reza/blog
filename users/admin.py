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