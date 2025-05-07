from django.db import models

class DexaAlmi(models.Model):
    id = models.BigAutoField(primary_key=True)
    kg_per_m2_yn = models.FloatField(null=True)
    kg_per_m2_am = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_almi_pkey'),
        ]
