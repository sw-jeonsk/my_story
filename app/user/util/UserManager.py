from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True  # 선택적으로 관리자를 마이그레이션으로 직렬화한다.
    # True로 설정된 경우 관리자가 마이그레이션으로 직렬화되며...?

    # 유저 생성
    # 파라미터로 전달받은 값들을 user 객체로 db에 저장한다
    # nomalize 중복 최소화를 위한 정규화?
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("이메일이 없습니다.")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    # 일반 유저 생성
    # 일반 사용자를 생성한다. is_staff, is_superuser = False ==> 일반유저라는 뜻
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("관리자는 is_staff가 True여야함")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("관리자는 is_superuser가 True여야함")

        return self._create_user(email, password, **extra_fields)
