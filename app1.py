from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Ale esta loco pa la verga"

app.run(debug=True, port=8000)