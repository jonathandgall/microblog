from flask import render_template
<<<<<<< HEAD
from app import app, db  # noqa F401
=======
from app import app, db
>>>>>>> fb050833acdb41647e7a939c66c88e8d08861c2a
from app.errors import bp

@bp.app_errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@bp.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500
