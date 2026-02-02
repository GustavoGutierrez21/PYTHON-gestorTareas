from django.db import models
from django.conf import settings 
import uuid

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Log(models.Model):
    id_log = models.BigAutoField(primary_key=True)
    id_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        related_name='logs'
    )
    host = models.CharField(max_length=255)
    ip = models.GenericIPAddressField()
    headers = models.JSONField(null=True, blank=True)  # Django 3.1+ soporta JSONField
    request_body = models.JSONField(null=True, blank=True)
    request_time = models.DateTimeField(auto_now_add=True)
    status_code = models.IntegerField()
    response_time = models.FloatField()  # Tiempo en segundos
    response_body = models.JSONField(null=True, blank=True)

    def __str__(self):
        return f"Log {self.id_log} - User {self.id_user}"