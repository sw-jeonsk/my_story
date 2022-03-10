from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from utils.writer_manager import WriterManager
from django.utils.translation import gettext_lazy as _
from utils.custom_field import hex_uuid, CaseLowerEmailField
from .validators import validate_email, validate_name, validate_password


class Writer(AbstractBaseUser, PermissionsMixin):
    objects = WriterManager()

    id = models.CharField(
        primary_key=True,
        unique=True,
        default=hex_uuid,
        editable=False,
        max_length=255,
    )
    email: str = CaseLowerEmailField(
        _("이메일"),
        max_length=64,
        unique=True,
        help_text="writer login ID",
        validators=[validate_email],
    )
    name: str = models.CharField(
        _("이름"),
        max_length=30,
        help_text="user name (firstname + second_name)",
        validators=[validate_name],
    )
    password = models.CharField(_("비밀번호"), max_length=128, validators=[validate_password])

    is_superuser: bool = models.BooleanField(_("관리자여부"), default=False)
    is_staff: bool = models.BooleanField(_("관리자페이지접속여부"), default=False)
    updated_at = models.DateTimeField(_("업데이트일"), default=timezone.now)
    created_at = models.DateTimeField(_("생성일"), default=timezone.now)

    # USERNAME_FIELD = 'email'로 이메일을 ID로 사용한다 명시해준다.
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    def __str__(self):
        return str(self.name)

    def get_short_name(self):
        return self.email

    class Meta:
        verbose_name = _("writer")
        verbose_name_plural = _("writers")
        db_table = "writer"
