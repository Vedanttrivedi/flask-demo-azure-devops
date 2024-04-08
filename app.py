import os
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

if __name__ == "__main__":
    app.run(host="0.0.0.0")
