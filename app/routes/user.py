
from fastapi import APIRouter, HTTPException
from models.beanie.user import User
from models.pydantic.user import SetNewUser, GetUserProfil
from services.user import create_new_user, check_email_is_available
from utils.logger import logger

router = APIRouter(prefix='/users', tags=['users'])

@router.get('/')
async def get_all_users():
    users = User.find_all()
    count = await User.count()

    return {
        "message": "all users from FastAPI!",
        "count": count,
        "data": users if count > 0 else []
    }

@router.post('/one')
async def get_one_user(input_data: GetUserProfil):
    target_user = await User.find_one(User.id == input_data.id)
    
    if not target_user:
        logger.warning(f"attempt to view a non-existent user {target_user.id}")
        raise HTTPException(
            status_code=404,
            detail="user not found!"
        )

    return {
        "message": "one user from FastAPI!",
        "data": target_user
    }

@router.post('/register')
async def register_user(input_data: SetNewUser):
    if not await check_email_is_available(input_data.email):
        logger.info("the user submitted an email address that is already in use")
        raise HTTPException(
            status_code=409,
            detail="email already used!"
        )
    
    new_user = await create_new_user(username=input_data.username, email=input_data.email)
    logger.info(f"new user save {new_user.id}")

    return {
        "message": "new user create from FastAPI!",
        "data": new_user
    }