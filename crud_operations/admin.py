from django.contrib import admin
from .import models

# Register your models here.
@admin.register(models.Info)
class InfoAdmin(admin.ModelAdmin):
    list_display=['name','address','phone_number']
    prepopulated_fields={"slug":('name','phone_number')}

