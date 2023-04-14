from abc import ABC

from django.core.validators import FileExtensionValidator

from djvue.serializers import FileUploadSerializer


class CSVUploadSerializer(FileUploadSerializer):
    """ Allows only CSV files to be uploaded """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file"].validators.append(FileExtensionValidator(allowed_extensions=['csv']))