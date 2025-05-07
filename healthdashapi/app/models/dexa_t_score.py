from django.db import models

class DexaTScore(models.Model):
    id = models.BigAutoField(primary_key=True)
    l_arm = models.FloatField(null=True)
    r_arm = models.FloatField(null=True)
    # ... (repeat for other fields)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)
