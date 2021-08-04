from rest_framework.exceptions import APIException


class EmailValidateException(APIException):
    status_code = 400
    detail_code = 400
    detail = "이메일이 잘못되었습니다."


class NameValidateException(APIException):
    status_code = 400
    detail_code = 400
    detail = "이름이 잘못되었습니다."
