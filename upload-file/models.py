import pymysql
import config

db = cursor = None


class Muploadfile():
    def __init__(self, id_file=None, nama_file=None, tgl_upload=None):
        self.id_file = id_file
        self.nama_file = nama_file
        self.tgl_upload = tgl_upload

    def openDB(self):
        global db, cursor
        db = pymysql.connect(host=config.DB_HOST, user=config.DB_USER,
                             password=config.DB_PASSWORD, database=config.DB_NAME)
        cursor = db.cursor()

    def closeDB(self):
        global db, cursor
        db.close()

# -----------
    def insertDB(self, data):
        self.openDB()
        cursor.execute(
            "INSERT INTO flask_upload ( nama_file, tgl_file) VALUES ('%s', '%s')" % data)
        db.commit()
        self.closeDB()
