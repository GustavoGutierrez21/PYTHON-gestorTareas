from django.db import models
import uuid

# Create your models here.


class UserRole(models.Model):
    id_user_role = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    name = models.CharField(
        max_length=50,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        db_table = "user_role"
        verbose_name = "User Role"
        verbose_name_plural = "User Roles"
