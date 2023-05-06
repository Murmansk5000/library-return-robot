import time
from board import SCL, SDA
import board
import busio
import digitalio
from adafruit_servokit import ServoKit

i2c0 = busio.I2C(board.SCL_1,board.SDA_1);

kit = ServoKit(channels=16,i2c = i2c0)
kit.servo[0].angle = 180
time.sleep(2)
