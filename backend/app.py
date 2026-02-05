from flask import Flask, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="database-1.cv6m8aiiqflt.eu-north-1.rds.amazonaws.com",
    user="admin",
    password="password",
    database="contactdb"
)

@app.route("/", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]

    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO contacts (name, email, message) VALUES (%s, %s, %s)",
        (name, email, message)
    )
    db.commit()

    return "Form submitted successfully"

app.run(host="0.0.0.0", port=5000)

