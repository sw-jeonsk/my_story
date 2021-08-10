import re
from utils.exceptions import (
    EmailRequiredException,
    NameValidateException,
    PasswordValidateException,
)
from django.contrib.auth.hashers import make_password


def validate_email(email):
    email_reg = r"[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(email):
        raise EmailRequiredException
    return email


def validate_name(name):
    if len(name) <= 2:
        raise NameValidateException
    return name


def validate_password(password):
    regex = "^(?=.*[A-Za-z])(?=.*\\d)(?=.*[~!@#$%^&*()+|=])[A-Za-z\\d~!@#$%^&*()+|=]{8,16}$"
    if not bool(re.match(regex, password)):
        raise PasswordValidateException
    return make_password(password)
