import RPi.GPIO as GPIO
import time

def make_sound(count=1):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	pwm_obj = GPIO.PWM(17,255)

	for i in range(count):
		pwm_obj.start(60)
		time.sleep(0.17)
		pwm_obj.start(0)
		time.sleep(0.17)

	GPIO.cleanup()
