from fastapi import (
    FastAPI,
    Request,
    status,
)
from fastapi.responses import JSONResponse

from app.core.exceptions import (
    ConflictError,
    PermissionDeniedError,
    ResourceNotFoundError,
)
from app.routers import (
    analytics,
    auth,
    health,
    post,
    user,
)


app = FastAPI(
    title="FastAPI User Management",
    version="0.2.0",
    description=(
        "User and post management API built with "
        "FastAPI, SQLAlchemy, PostgreSQL and JWT."
    ),
)


@app.exception_handler(
    ResourceNotFoundError
)
async def resource_not_found_handler(
    request: Request,
    exc: ResourceNotFoundError,
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "detail": exc.message,
        },
    )


@app.exception_handler(
    PermissionDeniedError
)
async def permission_denied_handler(
    request: Request,
    exc: PermissionDeniedError,
):
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={
            "detail": exc.message,
        },
    )


@app.exception_handler(
    ConflictError
)
async def conflict_handler(
    request: Request,
    exc: ConflictError,
):
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={
            "detail": exc.message,
        },
    )


app.include_router(
    health.router
)

app.include_router(
    auth.router
)

app.include_router(
    user.router
)

app.include_router(
    post.router
)

app.include_router(
    analytics.router
)


@app.get(
    "/",
    tags=["Default"],
)
def root():
    return {
        "message": (
            "FastAPI User Management is running"
        ),
        "docs": "/docs",
        "health": "/health",
    }