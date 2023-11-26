from django.contrib import admin
from . import models


# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ["your_firstname", "your_lastname", "your_email", "your_message"]


admin.site.register(models.Contact, ContactAdmin)
