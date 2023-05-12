from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from io import BytesIO
import qrcode

from django.core.files.uploadedfile import InMemoryUploadedFile

from .models import Patient, QRCode

def upload_document(request):
    if request.method == 'POST':
        name = request.POST['name']
        description = request.POST['description']
        documents = request.FILES.getlist('documents')
        
        patient = Patient.objects.create(name=name, description=description)
        
        for document in documents:
            patient.document = document
            patient.save()
            
            # Generate QR code
            qr_data = f'{patient.name}, {document.name}, {request.build_absolute_uri(reverse("document_detail", args=[patient.id]))}'
            qr_code = qrcode.make(qr_data)
            
            # Save QR code image
            buffer = BytesIO()
            qr_code.save(buffer, format='PNG')
            buffer.seek(0)
            qr_code_image = InMemoryUploadedFile(buffer, None, 'qr_code.png', 'image/png', buffer.getbuffer().nbytes, None)
            
            qr_code = QRCode.objects.create(patient=patient, code_image=qr_code_image)
            
        return HttpResponse('Documents uploaded successfully.')
    
    return render(request, 'upload_document.html')

def document_detail(request, id):
    patient = Patient.objects.get(id=id)
    context = {'patient': patient}
    return render(request, 'document_detail.html', context)
