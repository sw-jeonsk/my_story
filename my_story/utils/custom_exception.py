from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:
        response.data["status_code"] = response.status_code
        response.data["request"] = context["request"].data
        if hasattr(exc, "detail_code"):
            response.data["detail_code"] = exc.detail_code
    return response
