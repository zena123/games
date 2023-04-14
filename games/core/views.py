from django.shortcuts import render
from django.views.generic import TemplateView
from djvue.views import FileUploadView

from .serializers import CSVUploadSerializer


class CSVUploadView(FileUploadView):
    """add a view to for uploading a csv file"""
    serializer_class = CSVUploadSerializer


class HomeTemplateView(TemplateView):
    """ add template view to show homepage when running project"""
    template_name = 'home.html'

