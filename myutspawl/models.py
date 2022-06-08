import pymysql
import config
from flask_wtf import FlaskForm
from wtforms import StringField, StringField, StringField, SelectField, StringField, StringField, SubmitField, validators
#from wtforms.validators import Required, Length


class formulir_sks(FlaskForm):
    npm = StringField('NPM:',
                      validators=[validators.DataRequired('NPM harus diisi!'),
                                  validators.Length(max=25)])
    nama = StringField('Nama:',
                       validators=[validators.DataRequired('Nama harus diisi!'),
                                   validators.Length(max=25)])
    prodi = SelectField('Prodi:', choices=[
        (1, 'Sistem Informasi'),
        (2, 'Informatika'),
        (3, 'Teknologi Informasi'),
        (4, 'Teknik Industri'),
    ])
    ipk = StringField('IPK',
                      validators=[validators.DataRequired('IPK harus diisi!'),
                                  validators.Length(max=5)])
    sks = StringField('SKS',
                      validators=[validators.DataRequired('SKS harus diisi!'),
                                  validators.Length(max=3)])
    submit = SubmitField('Kirim')


db = cursos = None


class mahasiswa:
    def __init__(self, no=None, npm=None, nama=None, prodi=None, ipk=None, batasan=None):
        self.no = no
        self.npm = npm
        self.nama = nama
        self.prodi = prodi
        self.ipk = ipk
        self.batasan = batasan

    def openDB(self):
        global db, cursor
        db = pymysql.connect(
            host=config.DB_HOST, user=config.DB_USER, password=config.DB_PASSWORD, database=config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()

    def selectDB(self):
        self.openDB()
        cursor.execute("SELECT * FROM mahasiswa")
        container = []
        for npm, nama, prodi, ipk, batasan in cursor.fetchall():
            container.append((npm, nama, prodi, ipk, batasan))
        self.closeDB()
        return container

    def insertDB(self, data):
        self.openDB()
        cursor.execute(
            "INSERT INTO mahasiswa (no, npm, nama, prodi, ipk, batasan) VALUES ('%s','%s', '%s', '%s', '%s', '%s' )" % data)
        db.commit()
        self.closeDB()

    def getDBbyNo(self, no):
        self.openDB()
        cursor.execute("SELECT * FROM mahasiswa WHERE no='%s'" % no)
        data = cursor.fetchone()
        return data
