import re
from utils.exceptions import (
    EmailValidateException,
    NameValidateException,
    PasswordValidateException,
)
from django.contrib.auth.hashers import make_password


def validate_email(email):
    email_reg = r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[A-Za-z0-9](?:[A-Za-z0-9-]*[a-z0-9])?\.)+[A-Za-z0-9](?:[A-Za-z0-9-]*[A-Za-z0-9])?"
    regex = re.compile(email_reg)

    if not regex.match(email):
        raise EmailValidateException
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


def validate_required_check(data: dict, check_item: tuple):

    if not check_item[0] in data.keys() or len(data[check_item[0]]) < 1:
        raise check_item[1]
