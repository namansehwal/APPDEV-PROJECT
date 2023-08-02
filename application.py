from flask import Flask
import os
from flask_bootstrap import Bootstrap

current_dir = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = 'static/'


app = Flask(__name__)

app.config['SECRET_KEY'] = os.urandom(24)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


from authentication import *
from controller import *



if __name__ == '__main__':
    Bootstrap(app)
    app.run(debug=True)