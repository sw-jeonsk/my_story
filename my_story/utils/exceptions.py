from rest_framework.exceptions import APIException
from .response_detail import ResponseDetail


class Exception(APIException):
    detail_code = 200

    @classmethod
    def as_md(self, param=None):
        if param is None:
            return (
                '\n\n> **%s**\n```\n{\n\t"status_code": "%s"\n\t"detail_code": "%s"\n\t"detail": "%s"\n\t"items": []\n\t"request":{[request 데이터]}\n}\n```'
                % (self.status_code, self.status_code, self.detail_code, self.default_detail)
            )
        else:
            return (
                '\n\n> **%s**\n```\n{\n\t"status_code": "%s"\n\t"detail_code": "%s"\n\t"detail": "%s"\n\t"items": %s\n\t"request":{[request 데이터]}\n}\n```'
                % (self.status_code, self.status_code, self.detail_code, self.default_detail, param)
            )

    @classmethod
    def json_data(self, _detail=None):
        _data = dict()
        _data["status_code"] = self.status_code
        _data["detail_code"] = self.detail_code
        _data["default_detail"] = self.default_detail if _detail is None else _detail
        return _data


class Success(Exception):
    status_code = 200
    detail_code = "ok"
    default_detail = ResponseDetail.OK


class CreateSuccess(Exception):
    status_code = 201
    detail_code = "ok"
    default_detail = ResponseDetail.OK


class EmailRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.REQUIRED


class NameRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.REQUIRED


class PasswordRequiredException(Exception):
    status_code = 400
    detail_code = "required"
    default_detail = ResponseDetail.REQUIRED


class EmailValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.EMAIL_VALIDATE


class NameValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.NAME_VALIDATE


class PasswordValidateException(Exception):
    status_code = 400
    detail_code = "error"
    default_detail = ResponseDetail.PASSWORD_VALIDATE


class EmailDuplicateException(Exception):
    status_code = 400
    detail_code = "duplicate"
    default_detail = ResponseDetail.EMAIL_DUPLICATE


class UnauthorizedException(Exception):
    status_code = 401
    detail_code = "unauthorized"
    default_detail = ResponseDetail.UNAUTHORIZED_VALIDATE


class NotFoundWriterException(Exception):
    status_code = 404
    detail_code = "not_found"
    default_detail = ResponseDetail.NOTFOUND_WRITER
