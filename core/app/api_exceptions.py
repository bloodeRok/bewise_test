from rest_framework import status
from rest_framework.exceptions import APIException


class TooMuchAttempts(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = "Too many attempts." \
                     " Perhaps there are not so many unique questions left."
