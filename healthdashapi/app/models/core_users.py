from django.db import models

class CoreUser(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # enumerate the type field
    status= models.enums(null=True)
    type = models.enums(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_almi_pkey'),
        ]
