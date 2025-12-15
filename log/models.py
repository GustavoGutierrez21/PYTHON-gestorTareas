from django.db import models
import uuid

# Create your models here.


class Log(models.Model):

    id_log = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    # A futuro id_user

    host = models.CharField(max_length=255)
    ip = models.CharField(max_length=45)

    headers = models.JSONField()
    request_body = models.JSONField()

    request_time = models.DateTimeField()
    status_code = models.IntegerField()
    response_time = models.DateTimeField()

    response_body = models.JSONField()

    class Meta:
        db_table = "log"
        verbose_name = "Log"
        verbose_name_plural = "Logs"
