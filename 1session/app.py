from flask import Flask, render_template, session, request, redirect, url_for
from models import MPengguna

app = Flask(__name__)
app.config['SECRET_KEY'] = '1234567890'


@app.route('/')
def index():
    if 'username' in session:
        username = session['username']
        return render_template('index.html', username=username)
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        pengguna = MPengguna(username, password)
        if pengguna.authenticate():
            session['username'] = username
            return redirect(url_for('index'))
        msg = "username/password salah"
        return render_template('form.html', msg=msg)
    return render_template('form.html')


@app.route('/logout')
def logout():
    session.pop('username', ' ')
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
