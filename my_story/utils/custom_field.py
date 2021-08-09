import uuid
from django.db import models


def hex_uuid():
    """
    모델링 식별자 PK
    """
    return uuid.uuid4().hex


class CaseLowerEmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(CaseLowerEmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value
