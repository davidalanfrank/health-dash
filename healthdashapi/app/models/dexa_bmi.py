from django.db import models

class DexaBMI(models.Model):
    id = models.BigAutoField(primary_key=True)
    classification = models.CharField(max_length=255, null=True)
    bmi = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_bmi_pkey'),
        ]
