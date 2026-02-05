from flask import Flask, request
import mysql.connector
import os

app = Flask(__name__)

def get_db():
    return mysql.connector.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        password=os.environ.get("DB_PASS"),
        database=os.environ.get("DB_NAME"),
        connection_timeout=5
    )

@app.route("/", methods=["POST"])
def submit():
    try:
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
        return "Form submitted successfully"

    except Exception as e:
        return f"Database error: {str(e)}", 500

app.run(host="0.0.0.0", port=5000)
