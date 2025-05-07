from django.db import models

class DexaTotalMass(models.Model):
    id = models.BigAutoField(primary_key=True)
    l_arm = models.FloatField(null=True)
    r_arm = models.FloatField(null=True)
    trunk = models.FloatField(null=True)
    l_leg = models.FloatField(null=True)
    r_leg = models.FloatField(null=True)
    subtotal = models.FloatField(null=True)
    head = models.FloatField(null=True)
    total = models.FloatField(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)

    class Meta:
        constraints = [
            models.PrimaryKeyConstraint(fields=['id'], name='dexa_total_mass_pkey'),
        ]
