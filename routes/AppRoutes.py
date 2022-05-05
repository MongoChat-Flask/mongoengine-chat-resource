from flask import url_for
from werkzeug.utils import redirect

from app import app


@app.route('')
def startpoint():
    return redirect(url_for('UserRoutes.start'))
