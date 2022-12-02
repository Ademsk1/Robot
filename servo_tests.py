import RPi.GPIO as GPIO
import time


def servo_setup():
    GPIO.setMode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    servo = GPIO.PWM(7, 50)
    servo.start(0)
    return servo


servo = servo_setup()
servo.changeDutyCycle(2)
time.sleep(0.5)
servo.changeDutyCycle(0)
time.sleep(2)
duty = 2
while duty < 12:
    servo.changeDutyCycle(duty)
    time.sleep(0.5)
    duty += 1
    time.sleep(1.5)
