from django.db import models

class Blood(models.Model):
    blood_id = models.BigAutoField(primary_key=True)
    user_id = models.BigAutoField(null=True)
    document_id = models.models.BigAutoFields(null=True)
    marker_1 = models.BigAutoFields(null=True)
    marker_2 = models.BigAutoFields(null=True)
    