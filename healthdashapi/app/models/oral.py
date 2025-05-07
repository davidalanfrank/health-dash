from django.db import models

class Oral(models.Model):
    dexa_id = models.BigAutoField(primary_key=True)
    user_id = None
    document_id = models.BigAutoField(null=True)
    # not sure if this can be reduced to a single number
    attachment_loss_id = None
    pocket_depth_id = None
    plaque_idx_id = None

