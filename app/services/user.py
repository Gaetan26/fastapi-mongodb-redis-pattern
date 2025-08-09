
from models.beanie.user import User
from utils.user import harmonize_username

async def create_new_user(username: str, email: str):
    username = await harmonize_username(username)
    new_user = User(username=username, email=email)

    await new_user.create()

    return new_user

async def check_email_is_available(email: str):
    if await User.find_one(User.email == email):
        return False
    return True