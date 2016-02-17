from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.Name_Entity)
admin.site.register(models.Document)
admin.site.register(models.Context_Slice)
admin.site.register(models.User)
admin.site.register(models.Friends)
admin.site.register(models.Document_Entity)