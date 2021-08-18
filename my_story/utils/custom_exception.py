from rest_framework.exceptions import ErrorDetail
from rest_framework.views import exception_handler
from rest_framework import status
from .response_detail import ResponseDetail
import pdb


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    # Now add the HTTP status code to the response.

    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["request"] = context["request"].data
        response.data["items"] = list()
        if response.status_code in [status.HTTP_400_BAD_REQUEST, status.HTTP_404_NOT_FOUND]:
            if hasattr(exc, "detail_code"):
                response.data["detail_code"] = exc.detail_code
            else:
                for key, value in list(response.data.items()):

                    if not key in ["detail", "status_code", "request", "items"]:
                        error_detail = value if type(value) == ErrorDetail else value[0]
                        if type(error_detail) == ErrorDetail:
                            response.data["detail_code"] = error_detail.code
                        response.data["items"].append(key)
                        response.data["detail"] = "{}".format(error_detail)
                        del response.data[key]
        elif response.status_code == status.HTTP_401_UNAUTHORIZED:
            # case : 로그인할때,
            # case : token이 없거나 잘못됐을때,
            response.data["detail"] = ResponseDetail.UNAUTHORIZED_VALIDATE
            response.data["detail_code"] = "unauthorized"

    return response
