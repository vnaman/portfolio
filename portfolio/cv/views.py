from django.shortcuts import render
import os
from django.conf import settings
from django.http import HttpResponse, Http404
from portfolio.settings import BASE_DIR, MEDIA_ROOT
from django.core.files import File
from django.http import FileResponse

# Create your views here.
def home(request):
    return render(request, 'cv/home.html')

def DownloadPDF(self):
    path_to_file = MEDIA_ROOT + '/NamanVijayvargiya_Resume.pdf'
    f = open(path_to_file, 'rb')
    pdfFile = File(f)
    response = HttpResponse(pdfFile.read(), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment';
    return response
