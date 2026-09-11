from flask import Flask, render_template_string
import os
import psycopg2

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.environ.get("DB_HOST", "db"),
        database=os.environ.get("DB_NAME", "postgres"),
        user=os.environ.get("DB_USER", "postgres"),
        password=os.environ.get("DB_PASSWORD", "postgres")
    )
    return conn

@app.route('/')
def index():
    db_status = "<span style='color: #22c55e; font-weight: bold;'>Connected Successfully 🚀</span>"
    try:
        conn = get_db_connection()
        conn.close()
    except Exception as e:
        db_status = f"<span style='color: #ef4444; font-weight: bold;'>Failed: {str(e)}</span>"

    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Cloud Commerce Dashboard | DevOps Architecture</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; margin: 0; padding: 40px; }
            .container { max-width: 800px; margin: auto; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.3); }
            h1 { color: #38bdf8; font-size: 24px; border-bottom: 2px solid #334155; padding-bottom: 15px; }
            .card { background: #0f172a; padding: 20px; border-radius: 8px; margin-top: 20px; border-left: 5px solid #38bdf8; }
            .status { font-size: 18px; margin-top: 10px; }
            .badge { display: inline-block; padding: 6px 12px; border-radius: 20px; background: #334155; font-size: 14px; margin-bottom: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Cloud Commerce - DevOps Architecture Map</h1>
            <div class="badge">Multi-Stage Dockerfile + Docker Compose Orchestration</div>
            <div class="card">
                <h3>Backend API Service</h3>
                <p class="status">Database Status: {{ db_status | safe }}</p>
            </div>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_template, db_status=db_status)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
