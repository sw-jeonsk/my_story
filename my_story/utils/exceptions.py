from rest_framework.exceptions import APIException


class EmailRequiredException(APIException):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 필수입니다."


class EmailValidateException(APIException):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 잘못되었습니다."


class EmailDuplicateException(APIException):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 중복입니다."


class NameValidateException(APIException):
    status_code = 400
    detail_code = 400
    default_detail = "이름 잘못되었습니다."


class PasswordValidateException(APIException):
    status_code = 400
    detail_code = 400
    default_detail = "패스워드 잘못되었습니다."
