from django.db import models
## tbd, we might want to store a nights sleep rather than all data here
# class Sleep(models.Model):
#     sleep_id = models.BigAutoField(primary_key=True)
#     t_score_id = models.BigAutoField(null=True)
#     z_score_id = models.BigAutoField(null=True)
#     bmi_id = models.BigAutoField(null=True)
#     fat_id = models.BigAutoField(null=True)
#     fat_mass_height_squared = models.DecimalField(max_digits=10, decimal_places=2, null=True)
#     almi_id = models.BigAutoField(null=True)
#     lean_mass_id = models.BigAutoField(null=True)
#     lean_plus_bmc_id = models.BigAutoField(null=True)
#     total_mass_id = models.BigAutoField(null=True)
#     raw_location = models.CharField(max_length=255)
#     est_vat_id = models.BigAutoField(null=True)

#     class Meta:
#         constraints = [
#             models.PrimaryKeyConstraint(fields=['dexa_id'], name='dexa_pkey'),
#         ]
