from rest_framework.exceptions import APIException


class Exception(APIException):
    detail_code = 200

    @classmethod
    def as_md(self):
        return '\n\n> **%s**\n```\n{\n\t"status_code": "%s"\n\t"detail_code": "%s"\n\t"detail": "%s"\n\t"request":{[request 데이터]}\n}\n```' % (
            self.status_code,
            self.status_code,
            self.detail_code,
            self.default_detail,
        )


class EmailRequiredException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 필수입니다."


class NameRequiredException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "이름 필수입니다."


class PasswordRequiredException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "비밀번호 필수입니다."


class EmailValidateException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 잘못되었습니다."


class EmailDuplicateException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "이메일 중복입니다."


class NameValidateException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "이름 잘못되었습니다."


class PasswordValidateException(Exception):
    status_code = 400
    detail_code = 400
    default_detail = "패스워드 잘못되었습니다."
