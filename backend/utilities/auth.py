from sanic import response
from functools import wraps
import jwt
from config import SECRET_KEY

# Token required decorator
def token_required(f):
    @wraps(f)
    async def decorated_function(request, *args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return response.json({'error': 'Token is missing!'}, status=403)
        
        try:
            data = jwt.decode(token.split()[1], SECRET_KEY, algorithms=["HS256"])
            request.ctx.user_data = data  
        except Exception:
            return response.json({'error': 'Invalid Token!'}, status=403)
        
        return await f(request, *args, **kwargs)
    
    return decorated_function
