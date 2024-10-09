from sanic import Blueprint, response
from models.assignment import get_assignments, update_assignment_status
from models.user import authenticate_user,db
from models.user import create_user
from utilities.auth import token_required
from bson import ObjectId  

admin_bp = Blueprint('admin', url_prefix='/admin')


# Register admin
@admin_bp.route('/register', methods=['POST'])
async def register_admin(request):
    data = request.json
    await create_user(data['username'], data['password'], 'admin')
    return response.json({'message': 'Admin registered successfully'})


async def get_admin_name(admin_id):
    if isinstance(admin_id, str):
        admin_id = ObjectId(admin_id)   
    admin = await db.users.find_one({"_id": admin_id})
    if admin:
        return admin['username'] 
    return None  
# View Assignments
@admin_bp.route('/assignments', methods=['GET'])
@token_required
async def view_assignments(request):
    admin_id = request.ctx.user_data['user_id'] 
    
    
    admin_name = await get_admin_name(admin_id)
    if not admin_name:
        return response.json({'error': 'Admin not found'}, status=404)
     

    
    assignments = await get_assignments(admin_name)  
    return response.json({'assignments': assignments})


# Accept or reject assignments
@admin_bp.route('/assignments/<assignment_id>/<action>', methods=['POST'])
@token_required
async def update_assignment(request, assignment_id, action):
    if action not in ['accept', 'reject','pending']:
        return response.json({'error': 'Invalid action'}, status=400)
    
    await update_assignment_status(assignment_id, action)
    
    return response.json({'message': f'Assignment {action}ed successfully'})
