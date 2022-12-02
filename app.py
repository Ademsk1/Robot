import gpiozero
import time
from flask_cors import CORS
from flask import Flask, current_app, jsonify, request
robot = gpiozero.Robot(left=(27, 22), right=(17, 18))
app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def index():
    return current_app.send_static_file("index.html")


@app.route("/right", methods=['GET'])
def right():
    robot.right()
    return jsonify('ok')


@app.route("/left", methods=['GET'])
def left():
    robot.left()
    return jsonify('ok')


@app.route("/forward", methods=['GET'])
def forward():
    robot.forward()
    return jsonify('ok')


@app.route("/reverse", methods=['GET'])
def reverse():
    robot.backward()

    return jsonify('ok')


@app.route('/stop', methods=['GET'])
def stop():
    robot.stop()
    return jsonify('ok')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
