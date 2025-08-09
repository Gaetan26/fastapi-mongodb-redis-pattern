
async def harmonize_username(username: str):
    return username.lower().replace(' ', '_')