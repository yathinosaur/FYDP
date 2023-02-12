import RPi.GPIO as GPIO
import time

ZERO = 2.5
FULL_OPEN = 13
MIN_ANGLE = 0
MAX_ANGLE = 270

class Servo:
    def __init__(self, pinNum=17, freq=50):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinNum, GPIO.OUT)

        self.pwm = GPIO.PWM(pinNum, freq)
        # set servo open
        self.pwm.start(2.5)
    
    def setAngle(self, angle):
        assert angle >= MIN_ANGLE and angle <= MAX_ANGLE

        # open and closed should be between 90 and 270 degrees
        duty_cycle = (FULL_OPEN - ZERO) / MAX_ANGLE * angle + ZERO

        self.pwm.ChangeDutyCycle(duty_cycle)
    
    def cleanup(self):
        self.pwm.stop()
        GPIO.cleanup()


if __name__=="__main__":
    # example code
    servo = Servo()
    time.sleep(1)
    servo.setAngle(90)
    time.sleep(1)
    servo.cleanup()
