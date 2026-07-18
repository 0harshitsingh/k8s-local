import os
import time
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# Read settings passed down by Kubernetes environment variables
DB_HOST = os.getenv("DB_HOST", "postgres-service")
DB_NAME = os.getenv("POSTGRES_DB", "shopdb")
DB_USER = os.getenv("POSTGRES_USER", "shopadmin")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD", "supersecretpassword")

def get_db_connection():
    # Retry loop in case Postgres takes a few seconds to warm up
    for _ in range(5):
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return conn
        except psycopg2.OperationalError:
            time.sleep(2)
    return None

# Database Initialization: Create table & seed initial product if missing
conn = get_db_connection()
if conn:
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            item VARCHAR(100) NOT NULL,
            price NUMERIC(5,2) NOT NULL
        );
    ''')
    cur.execute("SELECT COUNT(*) FROM products;")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO products (item, price) VALUES (%s, %s);", 
                    ("Kubernetes Certified Pythonista Hoodie (Live DB!)", 59.99))
    conn.commit()
    cur.close()
    conn.close()

@app.route('/api/products')
def get_products():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "Could not connect to database"}), 500
    
    cur = conn.cursor()
    cur.execute("SELECT item, price FROM products LIMIT 1;")
    row = cur.fetchone()
    cur.close()
    conn.close()
    
    if row:
        return jsonify({"item": row[0], "price": float(row[1])})
    return jsonify({"error": "No items in the database"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)