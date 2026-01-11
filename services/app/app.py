import os
import psycopg2
from flask import Flask

DATABASE_URL = os.environ.get("DATABASE_URL", "postgresql://appuser:apppassword@postgres:5432/appdb")

app = Flask(__name__)

def get_conn():
    return psycopg2.connect(DATABASE_URL)

def init_db():
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("""                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    ts TIMESTAMP DEFAULT NOW()
                );
            """)
            conn.commit()

@app.route('/')
def index():
    init_db()
    with get_conn() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO visits DEFAULT VALUES RETURNING id, ts;")
            row = cur.fetchone()
            conn.commit()
            cur.execute("SELECT count(*) FROM visits;")
            total, = cur.fetchone()
    return f"✅ Hello from Flask! Visit #{row[0]} at {row[1]} — total visits: {total}\n"

if __name__ == '__main__':
    # For local debug only (compose uses gunicorn)
    app.run(host='0.0.0.0', port=8000)
