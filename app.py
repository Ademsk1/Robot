import gpiozero
import time
from flask import Flask, current_app, jsonify, request
robot = gpiozero.Robot(left=(17, 18), right=(27, 22))
app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return current_app.send_static_file("index.html")


@app.route('/right', methods=['GET'])
def right():
    robot.right()
    time.sleep(0.25)
    robot.stop()


@app.route('/left')
def left():
    robot.left()
    time.sleep(0.25)
    robot.stop()


@app.route('/forward')
def right():
    robot.right()
    time.sleep(0.25)
    robot.stop()


@app.route('/reverse')
def right():
    robot.reverse()
    time.sleep(0.25)
    robot.stop()


if __name__ == '__main__':
    app.run(debug=True)
