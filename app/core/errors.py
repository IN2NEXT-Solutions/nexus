import logging
from uuid import uuid4

from fastapi import FastAPI, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette import status
from starlette.exceptions import HTTPException as StarletteHTTPException


logger = logging.getLogger(__name__)


class AppError(Exception):
    def __init__(
        self,
        code: str,
        message: str,
        status_code: int = status.HTTP_400_BAD_REQUEST,
    ) -> None:
        self.code = code
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def _error_response(
    code: str,
    message: str,
    status_code: int,
    request_id: str,
) -> JSONResponse:
    return JSONResponse(
        status_code=status_code,
        content={
            "error": {
                "code": code,
                "message": message,
                "request_id": request_id,
            }
        },
    )


async def app_error_handler(request: Request, exc: AppError) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID", str(uuid4()))
    return _error_response(
        exc.code,
        exc.message,
        exc.status_code,
        request_id,
    )


async def http_error_handler(
    request: Request,
    exc: StarletteHTTPException,
) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID", str(uuid4()))

    if isinstance(exc.detail, str):
        message = exc.detail
    else:
        message = "The request could not be completed."

    return _error_response(
        "HTTP_ERROR",
        message,
        exc.status_code,
        request_id,
    )


async def validation_error_handler(
    request: Request,
    exc: RequestValidationError,
) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID", str(uuid4()))

    return _error_response(
        "VALIDATION_ERROR",
        "Request validation failed.",
        status.HTTP_422_UNPROCESSABLE_ENTITY,
        request_id,
    )


async def unhandled_error_handler(
    request: Request,
    exc: Exception,
) -> JSONResponse:
    request_id = request.headers.get("X-Request-ID", str(uuid4()))

    logger.exception(
        "Unhandled application error request_id=%s",
        request_id,
    )

    return _error_response(
        "INTERNAL_SERVER_ERROR",
        "An unexpected error occurred.",
        status.HTTP_500_INTERNAL_SERVER_ERROR,
        request_id,
    )


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(AppError, app_error_handler)
    app.add_exception_handler(StarletteHTTPException, http_error_handler)
    app.add_exception_handler(RequestValidationError, validation_error_handler)
    app.add_exception_handler(Exception, unhandled_error_handler)
