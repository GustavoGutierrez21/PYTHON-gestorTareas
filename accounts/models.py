from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)
from django.contrib.auth.hashers import make_password

import uuid

# region Enum status User
class UserStatus(models.TextChoices):
    ACTIVE = "ACTIVE", "Activo"
    INACTIVE = "INACTIVE", "Inactivo"
    BLOCKED = "BLOCKED", "Bloqueado"
    DELETED = "DELETED", "Eliminado"
# endregion


# region USER MANAGER
class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError("El usuario debe tener email")
        if not username:
            raise ValueError("El usuario debe tener username")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(email, username, password, **extra_fields)
# endregion


# Create your models here.

# ==========================================
# region Role
# ==========================================
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
    
    user_create = models.CharField(
        max_length=50,
        db_index=True
    )
    
    user_update = models.CharField(
        max_length=50,
        db_index=True
    )

    class Meta:
        db_table = "user_role"
        verbose_name = "User Role"
        indexes = [
            models.Index(fields=["id_user_role"]),
            models.Index(fields=["name"]),
            models.Index(fields=["user_create"]),
            models.Index(fields=["user_update"]),
        ]
        verbose_name_plural = "User Roles"
# endregion


# ==========================================
# region User
# ==========================================
class User(AbstractBaseUser, PermissionsMixin):
    id_user = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        db_index=True
    )

    id_user_role = models.ForeignKey(
        "UserRole",
        on_delete=models.PROTECT,
        related_name="users",
        db_column="id_user_role",
        db_index=True
    )
    
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(
        max_length=50,
        unique=True,
        db_index=True
    )
    email = models.EmailField(
        unique=True,
        db_index=True
    )
    password = models.CharField(max_length=128)
    
    # Estado
    status = models.CharField(
        max_length=20,
        choices=UserStatus.choices,
        default=UserStatus.ACTIVE,
        db_index=True
    )

    # Flags de permisos
    is_staff = models.BooleanField(default=False, db_index=True)
    is_superuser = models.BooleanField(default=False, db_index=True)

    # Auditoría
    last_login = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    user_create = models.CharField(
        max_length=50,
        db_index=True
    )
    
    user_update = models.CharField(
        max_length=50,
        db_index=True
    )
    
    # Manage
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        indexes = [
            models.Index(fields=["id_user"]),
            models.Index(fields=["id_user_role"]),
            models.Index(fields=["username"]),
            models.Index(fields=["email"]),
            models.Index(fields=["is_staff"]),
            models.Index(fields=["is_superuser"]),
            models.Index(fields=["user_create"]),
            models.Index(fields=["user_update"]),
        ]
        
    # =========================
    # METHODS
    # =========================
    def set_password(self, raw_password: str):
        self.password = make_password(raw_password)
    
    def __str__(self):
        return f"{self.username} ({self.email})"
