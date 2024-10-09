from sanic import Sanic
from routes.user import user_bp
from routes.admin import admin_bp
from sanic_cors import CORS

app = Sanic("AssignmentPortal")
CORS(app)
app.blueprint(user_bp)
app.blueprint(admin_bp)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000, debug=True)
