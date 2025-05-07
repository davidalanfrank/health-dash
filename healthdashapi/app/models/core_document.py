from django.db import models
from django.utils import timezone


class CoreDocument(models.Model):
    document_id = models.BigAutoField(primary_key=True)
    document_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255, null=True)
    doc_label_exception_id = models.BooleanField(null=True)
    name = models.CharField(max_length=255)
    file_type = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, default=timezone.now)
    updated_at = models.DateTimeField(null=True, default=timezone.now)
    
    class Meta:
        db_table='core_document'
        
