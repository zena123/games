from django.urls import path

from .views import CSVUploadView

app_name= 'core'

urlpatterns = [
    path("csv-upload/", CSVUploadView.as_view(), name="csv_upload"),
    ]