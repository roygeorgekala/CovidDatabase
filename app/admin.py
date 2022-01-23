from django.contrib import admin
from . models import *

# Register your models here.

admin.site.register(Quarantine_Info)
admin.site.register(Patient)
admin.site.register(Locality)
admin.site.register(Hospital)
admin.site.register(Close_Contact)
