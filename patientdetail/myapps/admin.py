from django.contrib import admin
from .models import Patient,QRCode

# Register your models here.
admin.site.register(Patient)
admin.site.register(QRCode)