import pdb
from utils.exceptions import EmailRequiredException


def validate_required(value):
    # whatever validation logic you need
    if value == "" or value is None:
        raise EmailRequiredException
