from django.db import models

class DexaFatMassHeightSquared(models.Model):
    id = models.BigAutoField(primary_key=True)
    kg_per_m2 = models.FloatField(null=True)
    android_gynoid_ratio = models.FloatField(null=True)
    fat_percent_trunk_legs = models.FloatField(null=True)
    trunk_limb_fat_mass_ratio = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_fat_mass_height_squared_pkey'),
        ]
