from django.contrib import admin
from . import models


admin.site.register(models.People)
admin.site.register(models.Publications)
admin.site.register(models.PublicationCategory)
admin.site.register(models.HomeSlider)