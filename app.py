from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return ("<HTML><BODY>Hello</BODY></HTML>")
    
app.run(debug=True)
