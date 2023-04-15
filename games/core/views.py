from django.shortcuts import render
from django.views.generic import TemplateView
from djvue.views import FileUploadView
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CSVUploadSerializer, HandleUploadSerializer


class CSVUploadView(FileUploadView):
    """add a view to for uploading a csv file"""
    serializer_class = CSVUploadSerializer


class HomeTemplateView(TemplateView):
    """ add template view to show homepage when running project"""
    template_name = 'home.html'


class HandleUploadView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request, format=None):
        serializer = HandleUploadSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
