from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Donor, Hospital, Admin

admin.site.register(Donor)
admin.site.register(Hospital)
admin.site.register(Admin)
