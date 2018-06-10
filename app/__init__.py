from flask import Flask

app = Flask(__name__)

from user_auth.routes import user_auth

app.register_blueprint(user_auth, url_prefix='/auth')
