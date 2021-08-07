from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='cv-home'),
    path('download/', views.DownloadPDF, name='download_pdf'),
]