from sanic import Blueprint, response
from models.user import create_user, authenticate_user,get_all_admins
from models.assignment import create_assignment,db
from utilities.auth import token_required

user_bp = Blueprint('user', url_prefix='/user')

# Register user
@user_bp.route('/register', methods=['POST'])
async def register(request):
    data = request.json
    await create_user(data['username'], data['password'], 'user')
    return response.json({'message': 'User registered successfully'})

# User login
@user_bp.route('/login', methods=['POST'])
async def login(request):
    data = request.json
    token = await authenticate_user(data['username'], data['password'])
    if token:
        return response.json({'token': token})
    return response.json({'error': 'Invalid credentials'}, status=401)

# Upload assignment
@user_bp.route('/upload', methods=['POST'])
@token_required
async def upload_assignment(request):
    data = request.json
    await create_assignment(data['userId'], data['task'], data['admin'])
    return response.json({'message': 'Assignment uploaded successfully'})
# View admins
@user_bp.route('/admins', methods=['GET'])
@token_required
async def fetch_all_admins(request):
    admins = await get_all_admins()  
    return response.json({'admins': admins})
