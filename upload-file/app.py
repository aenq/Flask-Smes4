from flask import Flask, render_template, request, redirect, url_for
from werkzeug.utils import secure_filename
from datetime import datetime
from models import Muploadfile
import os

application = Flask(__name__)
application.config['SECRET_KEY'] = '1234567890'
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = os.path.realpath('.') + \
    '/static/uploads'

# satuan byte
application.config['MAX_CONTENT_PATH'] = 10000000


@application.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        f = request.files['file']
        filename = application.config['UPLOAD_FOLDER'] + \
            '/' + secure_filename(f.filename)

        try:
            f.save(filename)
            return render_template('upload_sukses.html', filename=secure_filename(f.filename))
        except:
            return render_template('upload_gagal.html')
    return render_template('form.html')


if __name__ == '__main__':
    application.run(debug=True)
