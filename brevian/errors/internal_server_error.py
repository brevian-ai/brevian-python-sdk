# This file was auto-generated by Fern from our API Definition.

from ..core.api_error import ApiError
from ..types.internal_server_error_body import InternalServerErrorBody


class InternalServerError(ApiError):
    def __init__(self, body: InternalServerErrorBody):
        super().__init__(status_code=500, body=body)