from django.db import models

# should this be enum type ?
class CorePermissions(models.Model):
    perm_id = models.BigAutoField(primary_key=True)
    perm_code = models.CharField(max_length=50)
    perm_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

