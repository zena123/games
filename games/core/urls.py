from django.urls import path

from .views import CSVUploadView, HandleUploadView

app_name= 'core'

urlpatterns = [
    path("csv-upload/", CSVUploadView.as_view(), name="csv_upload"),
    path("import-data/", HandleUploadView.as_view(), name="import_data"),
    ]