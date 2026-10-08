class ApplicationError(Exception):
    """Base exception for application/business errors."""

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)


class ResourceNotFoundError(ApplicationError):
    """Requested resource does not exist."""


class PermissionDeniedError(ApplicationError):
    """Authenticated user is not allowed to perform the action."""


class ConflictError(ApplicationError):
    """Operation conflicts with the current resource state."""