from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Muestra"

app.run(debug=True, port=8000)