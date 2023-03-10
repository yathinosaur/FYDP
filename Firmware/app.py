import RPi.GPIO as GPIO
from flask import Flask, request, jsonify
import time

ZERO = 2.5
FULL_OPEN = 13
MIN_ANGLE = 0
MAX_ANGLE = 270

app = Flask(__name__)
pinNum = 17
freq = 50 

GPIO.setmode(GPIO.BCM)
GPIO.setup(pinNum, GPIO.OUT)

pwm = GPIO.PWM(pinNum, freq)

# set servo open
pwm.start(2.5)

@app.route('/')
def index():
    return 'HaptArmVR is cool'

@app.route('/servo/<int:angle>')
def setServoAngle(angle): 
    assert angle >= 0 and angle <= 270

    duty_cycle = (FULL_OPEN - ZERO) / MAX_ANGLE * angle + ZERO
    pwm.ChangeDutyCycle(duty_cycle)

    return "OK"


if __name__=="__main__":
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        pwm.stop()
        GPIO.cleanup()
