from motor.motor_asyncio import AsyncIOMotorClient
from bson.objectid import ObjectId
from config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client['assignment-submission']

# Create assignment
async def create_assignment(user_id, task, admin_id):
    assignment = {
        'user_id': user_id,
        'task': task,
        'admin_id': admin_id,
        'status': 'pending',
        
    }
    await db.assignments.insert_one(assignment)

# Get assignments for admin
async def get_assignments(admin_id):
    assignments = await db.assignments.find({'admin_id': admin_id}).to_list(length=100)
    for assignment in assignments:
        assignment['_id'] = str(assignment['_id'])
    return assignments

# Update assignment status
async def update_assignment_status(assignment_id, status):
    await db.assignments.update_one(
        {'_id': ObjectId(assignment_id)},
        {'$set': {'status': status}}
    )
