import gpiozero
import time
from flask import Flask, current_app, jsonify, request
robot = gpiozero.robot(left=(17, 18), right=(27, 22))
app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return current_app.send_static_file("index.html")


@app.route('/right', methods=['GET'])
def right():
    robot.right()
    time.sleep(0.25)
    robot.stop()
    return 'ok'


@app.route('/left', methods=['GET'])
def left():
    robot.left()
    time.sleep(0.25)
    robot.stop()
    return 'ok'


@app.route('/forward', methods=['GET'])
def forward():
    robot.right()
    time.sleep(0.25)
    robot.stop()
    return 'ok'


@app.route('/reverse', methods=['GET'])
def reverse():
    robot.reverse()
    time.sleep(0.25)
    robot.stop()
    return 'ok'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
