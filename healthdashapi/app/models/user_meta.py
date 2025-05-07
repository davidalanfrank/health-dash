from django.db import models

class CoreMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    # needs to be fk
    user_id = models.CharField(max_length=50)
    sign_up_time = models.DateTimeField(null=True, default=models.timezone.now)
    sign_up_method = enumerate()
    # need more work on this
    devices = models.IntegerField
    # enumerate the type field
    type = models.enums(null=True)
    last_active =  models.DateTimeField()
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_almi_pkey'),
        ]
