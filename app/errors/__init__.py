from flask import Blueprint
bp = Blueprint('errors', __name__)  # noqa E402
from app.errors import handlers  # noqa F401
