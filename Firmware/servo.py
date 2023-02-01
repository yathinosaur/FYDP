import RPi.GPIO as GPIO

class Servo:
    def __init__(self, pinNum=17, freq=50):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pinNum, GPIO.OUT)

        self.pwm = GPIO.PWM(pinNum, freq)
        # set servo open
        self.pwm.start(6.5)
    
    def setAngle(self, angle):
        # dont use this function yet
        assert angle >= 0 and angle <= 270

        duty_cyle = angle / 18

        self.pwm.ChangeDutyCycle(duty_cyle)
    
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
