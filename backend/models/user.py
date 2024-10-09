from motor.motor_asyncio import AsyncIOMotorClient
from config import MONGO_URI, SECRET_KEY
import jwt
import datetime

client = AsyncIOMotorClient(MONGO_URI)
db = client['assignment-submission']

# Create user (both user and admin)
async def create_user(username, password, role='user'):
    user = {
        'username': username,
        'password': password,  
        'role': role
    }
    await db.users.insert_one(user)

# Authenticate user
async def authenticate_user(username, password):
    user = await db.users.find_one({'username': username, 'password': password})
    if user:
        token = jwt.encode({
            'user_id': str(user['_id']),
            'role': user['role']
        }, SECRET_KEY, algorithm="HS256")
        return token
    return None

async def get_all_admins():
    admins = []
    async for admin in db.users.find({'role': 'admin'}): 
        admins.append({
            'id': str(admin['_id']),  
            'username': admin['username'], 
        })
    return admins