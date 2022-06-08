from flask import Flask, render_template, request, redirect, url_for
from models import formulir_sks, mahasiswa

app = Flask(__name__)
app.config['SECRET_KEY'] = '@#123456&*()'


@app.route('/', methods=['GET', 'POST'])
def index():
    form = formulir_sks()
    model = mahasiswa()
    container = []
    container = model.selectDB()
    if request.method == 'POST':
        # melakukan validasi data di dalam form
        if form.validate():
            npm = form.npm.data
            nama = form.nama.data
            prodi = int(form.prodi.data)
            ipk = float(form.ipk.data)
            sks = form.sks.data
            return render_template('response.html',
                                   npm=npm, nama=nama,
                                   prodi=prodi, ipk=ipk, sks=sks, container=container)

        else:
            # mengambil daftar kesalahan yang muncul
            # pada saat proses validasi
            errors = form.errors.items()
            return render_template('form.html',	form=form, errors=errors, container=container)

    return render_template('form.html', form=form, container=container)


if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/insert', methods=['GET', 'POST'])
# def insert():
#     if request.method == 'POST':
#         npm = request.form['npm']
#         nama = request.form['nama']
#         prodi = request.form['prodi']
#         ipk = request.form['ipk']
#         batasan = request.form['batasan']
#         data = (npm, nama, prodi, ipk, batasan)

#         model = mahasiswa()
#         model.insertDB(data)
#         return redirect(url_for('response'))

    # else:
    #     return render_template('insert_form.html')


if __name__ == '__main__':
    app.run(localhost=1234, debug=True)
