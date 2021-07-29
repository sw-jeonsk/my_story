from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .util.UserManager import UserManager
from django.utils.translation import gettext_lazy as _


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()

    email: str = models.EmailField(
        verbose_name="email id", max_length=64, unique=True, help_text="user login ID"
    )
    phone: str = models.CharField(max_length=100)
    address: str = models.CharField(max_length=100, null=True, blank=True, help_text="home address")
    name: str = models.CharField(max_length=30, help_text="user name (firstname + second_name)")
    create_at = models.DateTimeField(_("date joined"), default=timezone.now)

    # USERNAME_FIELD = 'email'로 이메일을 ID로 사용한다 명시해준다.
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def __str__(self):
        return str(self.name)

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        db_table = "user"
