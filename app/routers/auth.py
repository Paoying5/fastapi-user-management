from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import Token 
from app.core.security import create_access_token
from app.database import get_db
from app import crud
from app.schemas import LoginRequest
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from app.core.config import settings
from fastapi.security import OAuth2PasswordRequestForm

# Token của ứng dụng được lấy thông qua endpoint /auth/login
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

def get_current_user(

    token: str = Depends(oauth2_scheme),

    db: Session = Depends(get_db)

):

    credentials_exception = HTTPException(

        status_code=401,

        detail="Could not validate credentials"

    )

    try:

        payload = jwt.decode(

            token,

            settings.SECRET_KEY,

            algorithms=[settings.ALGORITHM]

        )

        email = payload.get("sub")

        if email is None:

            raise credentials_exception

        user = crud.get_user_by_email(

            db,

            email

        )

        if user is None:

            raise credentials_exception

        return user

    except JWTError:

        raise credentials_exception 

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# Tạo endpoint Login
@router.post(
    "/login",
    response_model=Token
)
def login(

    form_data: OAuth2PasswordRequestForm = Depends(),

    db: Session = Depends(get_db)

):

    user = crud.login_user(

        db,

        form_data.username,

        form_data.password

    )

    if not user:

        raise HTTPException(

            status_code=401,

            detail="Invalid email or password"

        )

    access_token = create_access_token(

    {

        "sub": user.email

    }

)

    return {

        "access_token": access_token,

        "token_type": "bearer"

}

@router.get("/me")
def read_me(

    current_user = Depends(get_current_user)

):

    return current_user