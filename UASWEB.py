from flask import Flask, render_template, jsonify
import pymysql

app = Flask(__name__)

# Koneksi ke database
def get_db_connection():
    return pymysql.connect(
        host='PROJEKUASWEB.mysql.pythonanywhere-services.com',  # Ganti username dengan akun PythonAnywhere Anda
        user='PROJEKUASWEB',                                   # Ganti username dengan akun PythonAnywhere Anda
        password='Dindaputri11',                # Ganti dengan password database Anda
        database='PROJEKUASWEB$all_products',                 # Ganti dengan nama database Anda di PythonAnywhere
        charset='utf8mb4',                                # Untuk mendukung karakter non-ASCII
        cursorclass=pymysql.cursors.DictCursor            # Mengembalikan hasil sebagai dictionary
    )

@app.route('/')
def index():
    # Koneksi ke database
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Ambil semua data produk dari database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    # Tutup koneksi
    cursor.close()
    connection.close()
    
    return render_template('index.html', products=products)

# API untuk produk
@app.route('/api/products')
def get_products():
    # Koneksi ke database
    connection = get_db_connection()
    cursor = connection.cursor()
    
    # Ambil semua data produk dari database
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    
    # Tutup koneksi
    cursor.close()
    connection.close()
    
    return jsonify(products)

if __name__ == '__main__':
    app.run()
