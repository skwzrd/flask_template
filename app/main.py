from flask import (
    Flask,
    render_template,
    url_for
)
import os
from config import IMG_PATH

app = Flask(__name__)
app.secret_key = str(os.urandom(32))
app.config['UPLOAD_FOLDER'] = IMG_PATH

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

@app.route('/', methods=['GET'])
def home():
    return render_template(
        'home.html'
    )

@app.route('/about', methods=['GET'])
def about():
    return render_template(
        'about.html'
    )

app.run(host='0.0.0.0', debug=True)
