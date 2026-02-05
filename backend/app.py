from flask import Flask, request, send_from_directory
import mysql.connector
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
        connection_timeout=5
    )

# GET → show HTML
@app.route("/", methods=["GET"])
def index():
    return send_from_directory(
        os.path.join(BASE_DIR, "frontend"),
        "1.html"
    )

# POST → save data
@app.route("/", methods=["POST"])
def submit():
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (
            request.form["name"],
            request.form["email"],
            request.form["message"]
        )
    )
    db.commit()
    return "Form submitted successfully ✅"

app.run(host="0.0.0.0", port=5000)
