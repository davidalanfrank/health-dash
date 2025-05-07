from django.db import models

class UserSignUpType(models.Model):
    sign_up_id = models.BigAutoField(primary_key=True)
    status_id = models.BigAutoField(primary_key=True)
    user_id = models
    # needs to be fk
    user_id = models.CharField(max_length=50)
    sign_up_time = models.DateTimeField(null=True, default=models.timezone.now)
    sign_up_method = enumerate()
    # need more work on this
    devices = models.IntegerField
    # enumerate the type field
    type = models.enums(null=True)
    created_at = models.DateTimeField(null=True, default=models.timezone.now)
    updated_at = models.DateTimeField(null=True, default=models.timezone.now)