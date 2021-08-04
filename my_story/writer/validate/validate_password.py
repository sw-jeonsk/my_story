from django.contrib.auth import password_validation
from django.core.exceptions import ValidationError

from utils.exceptions import PasswordValidateException

# from django.utils.translation import gettext as _
# from django.utils.translation import ngettext


def validate_password_check(password, writer=None, password_validators=None):
    """
    Validate whether the password meets all validator requirements.

    If the password is valid, return ``None``.
    If the password is invalid, raise ValidationError with all error messages.
    """
    special_character = "~`!@#$%&_=*()-^+"
    if password_validators is None:
        password_validators = password_validation.get_default_password_validators()
    for validator in password_validators:
        try:
            validator.validate(password, writer)

            if len(password) < 8:  # 패스워드 8자리 미만일 경우 raise
                raise PasswordValidateException
            if not any(char in special_character for char in password):  # 패스워드 특수문자 포함시키기,,
                raise PasswordValidateException

        except ValidationError as password_validate:
            raise PasswordValidateException from password_validate
