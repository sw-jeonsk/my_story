import uuid


def hex_uuid():
    """
    모델링 식별자 PK
    """
    return uuid.uuid4().hex
