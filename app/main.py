from fastapi import FastAPI
from app.routers import post
from app.routers import user, auth
from app.database import engine
from app.database import Base


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="FastAPI User Management"
)

app.include_router(
    user.router
)


app.include_router(auth.router)
app.include_router(post.router)


@app.get("/")
def root():
    return {
        "message":"FastAPI is running"
    }   