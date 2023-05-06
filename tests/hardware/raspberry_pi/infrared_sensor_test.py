#33 35 37 38 40
import RPi.GPIO as GPIO
import time
GPIO.cleanup()
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(33, GPIO.IN)
GPIO.setup(35, GPIO.IN)
GPIO.setup(37, GPIO.IN)
GPIO.setup(38, GPIO.IN)
GPIO.setup(40, GPIO.IN)

while True:
	
	time.sleep(0.5)
	print("left" , GPIO.input(33))
	#print("mid left" , GPIO.input(35))
	#print("mid" , GPIO.input(37))
	#print("mid right" , GPIO.input(38))
	#print("right" , GPIO.input(40))


	
