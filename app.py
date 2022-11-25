import gpiozero
import time
from flask import Flask, current_app, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file("index.html")


@app.route('/right', methods=['GET'])
def right():
    pass
