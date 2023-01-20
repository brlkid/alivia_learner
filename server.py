from flask import Flask
from flask import redirect, render_template, Request
app = Flask(__name__)

@app.route("/")
def home():
    return "It worked"

app.run(host="0.0.0.0", port=80, debug=True)