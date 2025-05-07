from django.db import models

class DexaEstVisAdiTissue(models.Model):
    id = models.BigAutoField(primary_key=True)
    est_vat = models.CharField(max_length=55, null=True)
    mass_g = models.BigIntegerField(null=True)
    volume_cm3 = models.BigIntegerField(null=True)
    area_cm2 = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_est_vis_adi_tissue_pkey'),
        ]
