from typing import Final


class ResponseDetail(object):
    EMAIL_REQUIRED: Final = "'email' 이 필드는 필수 항목입니다."
    NAME_REQUIRED: Final = "'name' 이 필드는 필수 항목입니다."
    PASSWORD_REQUIRED: Final = "'password' 이 필드는 필수 항목입니다."

    EMAIL_BLANK: Final = "'email' 이 필드는 blank일 수 없습니다."
    NAME_BLANK: Final = "'name' 이 필드는 blank일 수 없습니다."
    PASSWORD_BLANK: Final = "'password' 이 필드는 blank일 수 없습니다."

    EMAIL_VALIDATE: Final = "이메일 잘못되었습니다."
    NAME_VALIDATE: Final = "이름 잘못되었습니다."
    PASSWORD_VALIDATE: Final = "비밀번호 잘못되었습니다."

    EMAIL_DUPLICATE: Final = "이메일 중복입니다."

    LOGIN_VALIDATE: Final = "이메일 또는 패스워드가 잘못되었습니다."
    PERMISSION_VALIDATE: Final = "자격 권한에 문제가 있습니다."
