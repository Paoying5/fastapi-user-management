from fastapi import FastAPI

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


app.include_router(health.router)
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(post.router)
app.include_router(analytics.router)


@app.get(
    "/",
    tags=["Default"],
)
def root() -> dict[str, str]:
    return {
        "message": "FastAPI User Management is running",
        "docs": "/docs",
        "health": "/health",
    }