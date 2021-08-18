from django.utils import timezone
from writer.models import Writer
from django.db import models
from django.utils.translation import gettext_lazy as _
from utils.custom_field import hex_uuid

# Create your models here.
class Diary(models.Model):
    id = models.CharField(
        primary_key=True,
        unique=True,
        default=hex_uuid,
        editable=False,
        max_length=255,
    )
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE, related_name="writer")
    title = models.CharField(_("제목"), max_length=1024)
    contents = models.TextField(_("내용"))
    created_at = models.DateField(_("생성날짜"), default=timezone.now)
    updated_at = models.DateField(_("업데이트날짜"), default=timezone.now)

    class Meta:
        verbose_name = _("diary")
        verbose_name_plural = _("diarys")
        db_table = "diary"
