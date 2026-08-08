from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("MONGODB_URI"))

app = Flask(__name__)

client = MongoClient(os.getenv("MONGODB_URI"))
db = client["studentdb"]
collection = db["students"]

@app.route("/")
def form():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():

    student = {
        "name": request.form["name"],
        "email": request.form["email"]
    }

    collection.insert_one(student)

    return redirect("/success")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)