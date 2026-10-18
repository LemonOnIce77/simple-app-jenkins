from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def init_and_log_db():
    conn = sqlite3.connect('praktikum.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS log_kunjungan (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            pesan TEXT
        )
    ''')
    cursor.execute('INSERT INTO log_kunjungan (pesan) VALUES ("Akses berhasil dicatat ke database")')
    conn.commit()
    cursor.execute('SELECT COUNT(*) FROM log_kunjungan')
    total = cursor.fetchone()[0]
    conn.close()
    return total

@app.route('/')
def hello():
    total_kunjungan = init_and_log_db()
    return jsonify({
        "pesan": "Halo dari Flask + Database + Docker + Jenkins!",
        "status_database": "Terhubung (SQLite Database)",
        "total_data_tersimpan": total_kunjungan
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)