from flask import Flask

app = Flask(__name__)

from user_auth.views import user_auth
from messaging_service.views import messagingService

app.register_blueprint(user_auth, url_prefix='/auth')
app.register_blueprint(messagingService, url_prefix='/messagingService')