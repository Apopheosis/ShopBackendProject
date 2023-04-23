from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from utils.dependencies import get_current_user
from schemas import user
from utils import users_utils

router = APIRouter()

@router.post('/sign-up', response_model=user.User)
async def create_user(user: user.UserCreate):
    db_user = await users_utils.get_user_by_email(email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail='This email already registered')
    return await users_utils.create_user(user=user)

@router.post("/auth", response_model=user.TokenBase)
async def auth(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_utils.get_user_by_email(email=form_data.username)

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    if not users_utils.validate_password(
            password=form_data.password, hashed_password=user["hashed_password"]
    ):
        raise HTTPException(status_code=400, detail="Incorrect email or password")

    return await users_utils.create_user_token(user_id=user["id"])

@router.get("/users/me", response_model=user.UserBase)
async def read_users_me(current_user: user.User = Depends(get_current_user)):
    return current_user