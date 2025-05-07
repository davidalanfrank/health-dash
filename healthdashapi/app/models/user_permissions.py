from django.db import models

# there's probably a better way than storing
# and array of permission_ids as a field
# rather, we should extend this table with a new
# column which has a relationship to 
# a given perm in core_permissions
class UserPermissions(models.Model):
    user_perm_id = models.BigAutoField(primary_key=True)
    user_id = models.CharField(max_length=50)
    perm_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

