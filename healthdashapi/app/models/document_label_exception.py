from django.db import models

class DocumentLabelException(models.Model):
    exception_id = models.BigAutoField(primary_key=True)
    s3_loc = models.CharField(max_length=255)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)
