from .base import CustomException

from .general import (
    DatabaseException,
    DataInvalidException,
    LimitException,
    NotFoundException,
    DuplicateException,
    AuthorizationException,
)
from .handler import custom_exception_handler
