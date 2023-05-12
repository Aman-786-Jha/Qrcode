from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    document = models.FileField(upload_to='documents/')

class QRCode(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    code_image = models.ImageField(upload_to='qr_codes/')
