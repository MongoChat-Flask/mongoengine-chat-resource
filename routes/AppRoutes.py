from flask import url_for
from werkzeug.utils import redirect

import config


@config.app.route('')
def startpoint():
    return redirect(url_for('UserRoutes.start'))
