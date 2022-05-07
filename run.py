from app import app
from flask import url_for
from werkzeug.utils import redirect


@app.route('/')
def startpoint():
    return redirect(url_for('UserRoutes.start'))


if __name__ == '__main__':
    app.run(debug=True)
