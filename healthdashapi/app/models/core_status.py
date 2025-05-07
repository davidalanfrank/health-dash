from django.db import models

# should this be enum type ?
class CoreStatus(models.Model):
    status_id = models.BigAutoField(primary_key=True)
    status_code = models.CharField(max_length=50)
    status_name = models.CharField(max_length=50)
    entity_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

