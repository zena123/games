from djvue.fields import FileField
from rest_framework import serializers

from django.core.validators import FileExtensionValidator

from djvue.serializers import FileUploadSerializer
from rest_framework.reverse import reverse_lazy


class CSVUploadSerializer(FileUploadSerializer):
    """ Allows only CSV files to be uploaded """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].validators.append(FileExtensionValidator(allowed_extensions=['csv']))


class HandleUploadSerializer(serializers.Serializer):
    """ get uploaded file and call function to import data"""
    csv_file = FileField(style={"upload_url": reverse_lazy("csv_upload")})
